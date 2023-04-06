from enum import auto
from math import perm
import math
from django.shortcuts import redirect, render
from django.http import HttpResponse
from suivi.models import *
from suivi.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from dal import autocomplete
from django.utils.html import format_html
from django.template.defaulttags import register as reg

@reg.filter
def get_item(dictionary, key):
    return dictionary[key]

# Create your views here.

def index(request):
    
    return render(request,'suivi/index.html')

def home(request):
    return render(request, "registration/success.html", {})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('rechercheAffaire')

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('rechercheAffaire')
            else:
                return render(request, "accounts/login.html", {'form':form})
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login_view')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'admin/register.html', {'form': form})

@login_required
def affaire(request,id):
    affaire = Affaires.objects.get(id=id)
    id = affaire.id
    outils = Outils.objects.filter(id_affaires=affaire)
    ensembles = Ensembles.objects.filter(id_affaires=id)
    camions = Camions.objects.filter(id_affaires=id)
    factures = Factures.objects.filter(id_affaires=id)
    budget = Budget.objects.filter(id_affaires = id)
    commandes = Commandes.objects.filter(id_affaires = id).order_by('fournisseur')
    contacts = Contact.objects.filter(id_affaires = id)

    if request.method == 'POST':
        form = SearchPieceForm(request.POST)

        if form.is_valid():
            numero = form.cleaned_data['numero']
            if numero:
                print(numero)
                qs = PieceEnsemble.objects.get(id_affaires = affaire, id = numero)

                if qs:
                    if qs.type == 'piece':
                        piece = Pieces.objects.get(id = qs.id_piece.id)
                        return redirect('piece', piece.id)

                    if qs.type == 'ensemble':
                        ensemble = Ensembles.objects.get(id = qs.id_ensemble.id)
                        return redirect('ensemble', ensemble.id)

                    if qs.type == 'sousEnsemble':
                        sousEnsemble = SousEnsemble.objects.get(id = qs.id_sousensemble.id)
                        return redirect('sousEnsemble', sousEnsemble.id)

        return render(request, 'suivi/affaire.html',{'affaire':affaire, 'outils':outils, 'ensembles': ensembles, 'camions': camions, 'commandes':commandes, 'factures':factures, 'budget':budget, 'contacts':contacts, 'form':form})
    else:
        form = SearchPieceForm(initial={'id_affaires': affaire.id})
    return render(request,'suivi/affaire.html',{'affaire':affaire,'outils':outils,'ensembles':ensembles,'camions':camions,'factures':factures, 'commandes':commandes, 'budget':budget, 'contacts':contacts, 'form':form})

@login_required
def outil(request,id):
    outil = Outils.objects.get(id=id)
    affaire = Affaires.objects.get(id= outil.id_affaires.id)
    ensembles = Ensembles.objects.filter(id_outils = outil.id)
    nomenclature = Nomenclature.objects.filter(id_affaires = affaire, id_outils = id)
    dictionnaire_SE = {}
    dictionnaire_E= {}
    for ensemble in ensembles:
        avancement_E = AvancementEnsemble.objects.filter(id_ensembles = ensemble.id)
        sous_ensemble = SousEnsemble.objects.filter(id_ensemble = ensemble.id)
        dictionnaire_SE[ensemble] = sous_ensemble
        dictionnaire_E[ensemble] = avancement_E

    return render(request, 'suivi/outil.html', {'outil':outil,'affaire':affaire,'ensembles':ensembles, 'nomenclature':nomenclature, 'dictionnaire_SE':dictionnaire_SE, 'dictionnaire_E': dictionnaire_E})

@login_required    
def ensemble(request,id):
    ensemble = Ensembles.objects.get(id=id)
    affaire = Affaires.objects.get(id=ensemble.id_affaires.id)
    outil = Outils.objects.get(id=ensemble.id_outils.id)
    sousEnsembles = SousEnsemble.objects.filter(id_ensemble = ensemble.id)
    pieces = Pieces.objects.filter(id_ensemble=ensemble.id)
    avancement = AvancementEnsemble.objects.filter(id_ensembles = ensemble)
    return render(request, 'suivi/ensemble.html',{'ensemble':ensemble, 'sousEnsembles':sousEnsembles ,'outil':outil,'affaire':affaire, 'pieces':pieces, 'avancement':avancement})

@login_required
def sousEnsemble(request,id):
    sousEnsemble = SousEnsemble.objects.get(id = id)
    avancement = AvancementSousEnsemble.objects.get(id_sousensemble = sousEnsemble)
    affaire = sousEnsemble.id_affaires
    outil = sousEnsemble.id_outils
    ensemble = sousEnsemble.id_ensemble
    pieces = Pieces.objects.filter(id_sous_ensemble = sousEnsemble.id)
    return render(request, 'suivi/sousEnsemble.html',{'affaire':affaire,'outil':outil,'ensemble':ensemble,'sousEnsemble':sousEnsemble, 'pieces':pieces, 'avancement':avancement})


@login_required
def piece(request,id):
    piece = Pieces.objects.get(id=id)
    sousEnsemble = piece.id_sous_ensemble
    ensemble = Ensembles.objects.get(id=piece.id_ensemble.id)
    affaire = Affaires.objects.get(id=piece.id_affaires.id)
    outil = Outils.objects.get(id=piece.id_outil.id)
    return render(request, 'suivi/piece.html',{'piece':piece,'ensemble':ensemble,'outil':outil,'affaire':affaire, 'sousEnsemble':sousEnsemble})

@login_required
def nomenclature(request,id):
    nomenclature = Nomenclature.objects.get(id = id)
    affaire = Affaires.objects.get(id = nomenclature.id_affaires.id)
    outil = nomenclature.id_outils
    ensembles = Ensembles.objects.filter(id_outils = nomenclature.id_outils)
    dictionnaire_SE = {}
    dictionnaire_avancement = {}
    for ensemble in ensembles:
        sousEnsembles = SousEnsemble.objects.filter(id_ensemble = ensemble)
        dictionnaire_SE[ensemble.id] = sousEnsembles
        avancement = AvancementEnsemble.objects.get(id_ensembles = ensemble)
        dictionnaire_avancement[ensemble] = avancement

    return render(request, 'suivi/nomenclature.html', {'affaire':affaire, 'outil':outil, 'ensembles':ensembles, 'dictionnaire_SE': dictionnaire_SE, 'dictionnaire_avancement': dictionnaire_avancement, 'affaire':affaire})


@login_required
def camion(request,id):
    camion = Camions.objects.get(id=id)
    chargements = Chargementcamions.objects.filter(id_camions = camion)
    affaire = Affaires.objects.get(id=camion.id_affaires.id)
    if request.method == 'POST':
        form = SearchPieceForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
            piece1 = PieceEnsemble.objects.get(id=numero)

            if piece1.type == 'piece':
                piece = Pieces.objects.get(id=piece1.id_pieces.id)
                chargement = Chargementcamions(
                    identifiant_camion = camion.identifiant,
                    numero_piece = piece.numero,
                    quantite_piece = piece.quantite,
                    poids_total = piece.poids_unitaire * piece.quantite,
                    id_camions = camion,
                    id_pieces = piece,
                    id_affaires = affaire
                    )
                chargement.save()

            if piece1.type == 'sousEnsemble':
                piece = SousEnsemble.objects.get(id = piece1.id_sousensemble.id)
                chargement = Chargementcamions(
                    identifiant_camion = camion.identifiant,
                    numero_piece = piece.numero,
                    quantite_piece = 1,
                    poids_total = piece.quantite * piece.poids,
                    id_camions = camion,
                    id_sous_ensemble = piece,
                    id_affaires = affaire,
                )
                chargement.save()

            chargements = Chargementcamions.objects.filter(id_camions = camion)
            return render(request,'suivi/camion.html', {'form':form,'id':id, 'camion':camion, 'chargementCamion':chargements, 'affaire':affaire})

    else:
        form = SearchPieceForm(initial={'id_affaires': affaire.id})

    return render(request,'suivi/camion.html',{'form':form,'id':id, 'camion':camion, 'chargementCamion':chargements, 'affaire':affaire})

@login_required
def commande(request,id):
    commande = Commandes.objects.get(id=id)
    return render(request, 'suivi/commande.html',{'commande':commande})

@login_required
def facture(request,id):
    facture = Factures.objects.get(id=id)
    affaire = facture.id_affaires
    return render(request,'suivi/facture.html',{'facture':facture, 'affaire':affaire})

def rechercheFacture(request):
    if request.method == 'POST':
        form = RechercheFactureForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['numero']:
                factures = Factures.objects.filter(id__icontains=form.cleaned_data['numero'])
            
            if factures:
                return render(request,'suivi/rechercheFacture.html',{'form':form, 'factures':factures})

    else:
        form = RechercheFactureForm()
        
    return render(request,'suivi/rechercheFacture.html',{'form':form})


def rechercheAffaire(request):
    if request.method == 'POST':
        form = SearchAffaireForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['numero']:
                affaire = Affaires.objects.get(id=form.cleaned_data['numero'])
                
            if affaire:
                return redirect('affaire', id=affaire.id)

        else:
            print(form.errors)
        
    form = SearchAffaireForm()

    return render(request,'suivi/rechercheAffaire.html',{'form': form})

def rechercheCamion(request):
    if request.method == 'POST':
        form = SearchCamionForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['identifiant']:
                camion = Camions.objects.get(id=form.identifiant)
                return redirect('camion',id=camion.id)
    
    form = RechercheCamionForm()

    return render(request,'suivi/rechercheCamion.html',{'form':form})

def rechercheCommande(request):
    if request.method == 'POST':
        form = SearchCommandeForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['numero']:
                commande = Commandes.objects.get(id = form.cleaned_data['numero'])

                return redirect('commande', id = commande.id)
    
    form = SearchCommandeForm()

    return render(request,'suivi/rechercheCommande.html',{'form':form})

@login_required
@permission_required('suivi.change_factures', raise_exception=True)
def lierFacture(request,id):
    facture = Factures.objects.get(id=id)

    if request.method == 'POST':
        form = SearchFactureForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['numero']:
                facture2 = Factures.objects.get(id=form.cleaned_data['numero'])
                facture.paired_factures.add(facture2)

                return redirect('facture', id=facture.id)

    form = SearchFactureForm()
    return render(request,'suivi/lierFacture.html',{'form':form, 'facture':facture})

@login_required
@permission_required('suivi.change_commandes', raise_exception=True)
def lierCommande(request,id):
    commande = Commandes.objects.get(id=id)

    if request.method == 'POST':
        form = SearchCommandeForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['numero']:
                commande2 = Commandes.objects.get(id=form.cleaned_data['numero'])
                commande.paired_factures.add(commande2)

                return redirect('commande', id=commande.id)

    form = SearchCommandeForm()
    return render(request,'suivi/lierCommande.html',{'form':form, 'commande':commande})

@login_required
@permission_required('suivi.change_affaires', raise_exception=True)
def editAffaire(request,id):
    affaire = Affaires.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditAffaireForm(request.POST,instance=affaire)
        if form.is_valid():
            affaire = form.save()
            return redirect('affaire',affaire.id)
    else:
        form = EditAffaireForm(instance=affaire)

    return render(request,'suivi/editAffaire.html',{'form':form,'affaire':affaire})

@login_required
@permission_required('suivi.add_affaires', raise_exception=True)
def createAffaire(request):
    if request.method == 'POST':
        form = EditAffaireForm(request.POST)

        if form.is_valid():
            affaire = form.save()
            affaires = Affaires.objects.get(id = affaire.id)
            budget = Budget(id_affaires = affaires)
            budget.save()

            return redirect('affaire', affaire.id)
    else:
        form = EditAffaireForm()
    
    return render(request,'suivi/createAffaire.html', {'form': form})

@login_required
@permission_required('suivi.change_outils', raise_exception=True)
def editOutil(request,id):
    outil = Outils.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditOutilForm(request.POST,instance=outil)
        if form.is_valid():
            outil = form.save()
            return redirect('outil',outil.id)
    else:
        form = EditOutilForm(instance=outil)

    return render(request,'suivi/editOutil.html',{'form':form,'outil':outil})

@login_required
@permission_required('suivi.add_outils', raise_exception=True)
def createOutil(request,id_affaires):
    affaire = Affaires.objects.get(id = id_affaires)
    if request.method == 'POST':
        form = EditOutilForm(request.POST)
        

        if form.is_valid():
            outil = form.save(commit=False)
            outil.id_affaires = affaire

            outil = form.save()

            return redirect('outil', outil.id)
    else:
        form = EditOutilForm()
    
    return render(request,'suivi/createOutil.html', {'form': form})

@login_required
@permission_required('suivi.change_ensembles', raise_exception=True)
def editEnsemble(request,id):
    ensemble = Ensembles.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditEnsembleForm(request.POST,instance=ensemble)
        piece_ensemble = PieceEnsemble.objects.get(id_ensemble = id)
        avancementEnsemble = AvancementEnsemble.objects.get(id_ensembles = ensemble)
        if form.is_valid():
            ensemble = form.save()
            piece_ensemble.nom = ensemble.nom
            piece_ensemble.numero = ensemble.numero
            avancementEnsemble.numero_ensemble = ensemble.numero
            
            piece_ensemble.save()
            avancementEnsemble.save()
            return redirect('ensemble',ensemble.id)
    else:
        form = EditEnsembleForm(instance=ensemble)

    return render(request,'suivi/editEnsemble.html',{'form':form,'ensemble':ensemble})

@login_required
@permission_required('suivi.add_ensembles',raise_exception=True)
def createEnsemble(request,id_affaire,id_outil):
    if request.method == 'POST':
        form = CreateEnsembleForm(request.POST)
        affaire = Affaires.objects.get(id = id_affaire)
        outil = Outils.objects.get(id = id_outil)

        if form.is_valid():
            ensemble = form.save(commit=False)

            ensemble.id_affaires = affaire
            ensemble.id_outils = outil

            ensemble = form.save()

            id_ensemble = Ensembles.objects.get(id=ensemble.id)

            avancement_ensemble = AvancementEnsemble(id_affaires = affaire, id_ensembles = id_ensemble)
            piece_ensemble = PieceEnsemble(nom = ensemble.nom, numero = ensemble.numero, type = 'ensemble', id_affaires = affaire, id_ensemble = id_ensemble)

            piece_ensemble.save()
            avancement_ensemble.save()

            return redirect('ensemble', ensemble.id)
    else:
        form = CreateEnsembleForm()
    
    return render(request,'suivi/createEnsemble.html', {'form': form})

@login_required
@permission_required('suivi.change_sousensemble', raise_exception = True)
def editSousEnsemble(request,id):
    sousEnsemble = SousEnsemble.objects.get(id=id)
    piece_ensemble = PieceEnsemble.objects.get(id_sousensemble = sousEnsemble)

    if request.method == 'POST':
        form = EditSousEnsembleForm(request.POST, instance= sousEnsemble)
        avancementSousEnsemble = AvancementSousEnsemble.objects.get(id_sousensemble = sousEnsemble)

        if form.is_valid():
            sousEnsemble = form.save()

            avancementSousEnsemble.numero_sousensemble = sousEnsemble.numero
            avancementSousEnsemble.save()

            piece_ensemble.nom = sousEnsemble.nom
            piece_ensemble.numero = sousEnsemble.numero

            piece_ensemble.save()

            return redirect('sousEnsemble', sousEnsemble.id)

    else:
        form = EditSousEnsembleForm(instance = sousEnsemble)
        
    return render(request, 'suivi/editSousEnsemble.html', {'form':form,'sousEnsemble':sousEnsemble})

@login_required
@permission_required('suivi.add_sousensemble',raise_exception=True)
def createSousEnsemble(request,id_ensembles):

    ensemble = Ensembles.objects.get(id = id_ensembles)
    affaire = ensemble.id_affaires
    outil = ensemble.id_outils

    if request.method == 'POST':
        form = CreateSousEnsembleForm(request.POST)

        if form.is_valid():
            sousEnsemble = form.save(commit = False)

            sousEnsemble.id_affaires = affaire
            sousEnsemble.id_outils = outil
            sousEnsemble.id_ensemble = ensemble

            sousEnsemble = form.save()
            id_sousensemble = sousEnsemble.id

            sousEnsemble = SousEnsemble.objects.get(id=id_sousensemble)

            avancement = AvancementSousEnsemble(id_affaires = affaire, id_sousensemble = sousEnsemble, id_ensemble = ensemble)
            avancement.save()

            piece_ensemble = PieceEnsemble(nom = sousEnsemble.nom, numero = sousEnsemble.numero, id_sousensemble = sousEnsemble, id_affaires = affaire, type = 'sousEnsemble')
            piece_ensemble.save()

            return redirect('sousEnsemble', sousEnsemble.id)
 
    form = CreateSousEnsembleForm()

    return render(request, 'suivi/createSousEnsemble.html', {'form':form,'ensemble':ensemble})
        

@login_required
@permission_required('suivi.change_pieces', raise_exception=True)
def editPiece(request,id):
    piece = Pieces.objects.get(id=id)
    piece_ensemble = PieceEnsemble.objects.get(id_piece = id)
    
    if request.method == 'POST':
        form = EditPieceForm(request.POST,instance=piece)

        if form.is_valid():
            piece = form.save()

            piece_ensemble.nom = piece.nom
            piece_ensemble.numero = piece.numero

            piece_ensemble.save()

            return redirect('piece',piece.id)
    else:
        form = EditPieceForm(instance=piece)

    return render(request,'suivi/editPiece.html',{'form':form,'piece':piece})

@login_required
@permission_required('suivi.add_pieces', raise_exception=True)
def createPiece(request, id_sousEnsemble):
    if request.method == 'POST':
        sousEnsemble = SousEnsemble.objects.get(id=id_sousEnsemble)
        form = EditPieceForm(request.POST)
        affaire = Affaires.objects.get(id = sousEnsemble.id_affaires.id)
        outil = Outils.objects.get(id = sousEnsemble.id_outils.id)
        ensemble = Ensembles.objects.get(id = sousEnsemble.id_ensemble.id)
        

        if form.is_valid():
            piece = form.save(commit=False)
            
            piece.numero_outil = outil.numero
            piece.numero_ensemble = ensemble.numero
            piece.numero_affaire = affaire.numero
            piece.id_affaires = affaire
            piece.id_outil = outil
            piece.id_ensemble = ensemble
            piece.id_sous_ensemble = sousEnsemble
            piece = form.save()
            pieces = Pieces.objects.get(id=piece.id)
            piece_ensemble = PieceEnsemble(nom = pieces.nom, numero = pieces.numero, id_piece = pieces, id_affaires = affaire, type = 'piece')
            
            piece_ensemble.save()

            return redirect('piece', piece.id)
    else:
        form = EditPieceForm()
    
    return render(request,'suivi/createPiece.html', {'form': form})

@login_required
@permission_required('suivi.change_camions', raise_exception=True)
def editCamion(request,id):
    camion = Camions.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditCamionForm(request.POST,instance=camion)
        if form.is_valid():
            piece = form.save()
            return redirect('camion',camion.id)
    else:
        form = EditCamionForm(instance=camion)

    return render(request,'suivi/editCamion.html',{'form':form,'camion':camion})

@login_required
@permission_required('suivi.add_camions', raise_exception=True)
def createCamion(request,id_affaire):
    if request.method == 'POST':
        form = CreateCamionForm(request.POST)
        affaire = Affaires.objects.get(id = id_affaire)

        if form.is_valid():
            camion = form.save(commit=False)
            camion.id_affaires = affaire
            camion = form.save()

            return redirect('camion', camion.id)
    else:
        form = CreateCamionForm()
    
    return render(request,'suivi/createCamion.html', {'form': form})

@login_required
@permission_required('suivi.change_chargementcamion', raise_exception=True)
def editChargementCamion(request,id):
    chargement = Chargementcamions.objects.get(id=id)
    camion = Camions.objects.get(id=chargement.id_camions.id)
    if chargement.id_pieces:
        poids_unitaire = chargement.id_pieces.poids_unitaire
    if chargement.id_sous_ensemble:
        poids_unitaire = chargement.id_sous_ensemble.poids
    
    if request.method == 'POST':
        form = EditChargementCamionForm(request.POST,instance=chargement)
        if form.is_valid():
            chargement = form.save(commit=False)
            chargement.poids_total = poids_unitaire * form.cleaned_data['quantite_piece']
            chargement.save()
            return redirect('camion', camion.id)
    else:
        form = EditChargementCamionForm(instance=chargement)

    return render(request,'suivi/editChargementCamion.html',{'form':form,'chargementCamion':chargement, 'camion':camion})

@login_required
@permission_required('suivi.change_factures', raise_exception=True)
def editFacture(request,id):
    facture = Factures.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditFactureForm(request.POST,instance=facture)
        if form.is_valid():
            facture = form.save()
            return redirect('facture',facture.id)
    else:
        form = EditFactureForm(instance=facture)

    return render(request,'suivi/editFacture.html',{'form':form,'facture':facture})

@login_required
@permission_required('suivi.add_factures', raise_exception=True)
def createFacture(request,id_affaire):
    if request.method == 'POST':
        form = EditFactureForm(request.POST)
        affaire = Affaires.objects.get(id = id_affaire)

        if form.is_valid():
            facture = form.save(commit=False)
            
            facture = form.save()
            facture1 = Factures.objects.get(id = facture.id)
            facture1.id_affaires.add(affaire)
            return redirect('facture', facture.id)
    else:
        form = EditFactureForm()
    
    return render(request,'suivi/createFacture.html', {'form': form})

@login_required
@permission_required('suivi.change_commandes', raise_exception=True)
def editCommande(request,id):
    commande = Commandes.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditCommandeForm(request.POST,instance=commande)
        if form.is_valid():
            commande = form.save()
            return redirect('commande',commande.id)
    else:
        form = EditCommandeForm(instance=commande)

    return render(request,'suivi/editCommande.html',{'form':form,'commande':commande})

@login_required
@permission_required('suivi.add_commandes', raise_exception=True)
def createCommande(request,id_affaires):
    affaire = Affaires.objects.get(id = id_affaires)
    if request.method == 'POST':
        form = EditCommandeForm(request.POST)

        if form.is_valid():
            commande = form.save(commit=False)
            commande = form.save()
            commande1 = Commandes.objects.get(id = commande.id)
            commande1.id_affaires.add(affaire)

            return redirect('commande', commande.id)
    else:
        form = EditCommandeForm()
    
    return render(request,'suivi/createCommande.html', {'form': form, 'affaire':affaire})

@login_required
@permission_required('suivi.add_nomenclature', raise_exception=True)
def createNomenclature(request, id_affaire, id_outil):
    affaire = Affaires.objects.get(id = id_affaire)
    outil = Outils.objects.get(id = id_outil)

    if request.method == 'POST':
        form = EditNomenclatureForm(request.POST)

        if form.is_valid():
            nomenclature = form.save(commit = False)
            nomenclature.id_affaires = affaire
            nomenclature.id_outils = outil
            nomenclature = form.save()

            return redirect('nomenclature', nomenclature.id)
    else:
        form = EditNomenclatureForm()
    
    return render(request,'suivi/createNomenclature.html', {'form': form})

@login_required
@permission_required('suivi.change_nomenclature', raise_exception=True)
def editNomenclature(request,id):
    nomenclature = Nomenclature.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditNomenclatureForm(request.POST,instance=nomenclature)
        if form.is_valid():
            nomenclature = form.save()
            return redirect('nomenclature',nomenclature.id)
    else:
        form = EditNomenclatureForm(instance=nomenclature)

    return render(request,'suivi/editNomenclature.html',{'form':form,'nomenclature':nomenclature})

@login_required
@permission_required('suivi.add_anomalies', raise_exception=True)
def createAnomalie(request):
    if request.method == 'POST':
        form = EditAnomalieForm(request.POST)

        if form.is_valid():
            anomalie = form.save()

            return redirect('Anomalie', anomalie.id)
    else:
        form = EditAnomalieForm()
    
    return render(request,'suivi/createAnomalie.html', {'form': form})

@login_required
@permission_required('suivi.change_anomalies', raise_exception=True)
def editAnomalie(request,id):
    anomalie = Anomalies.objects.get(id=id)
    
    if request.method == 'POST':
        form = EditAnomalieForm(request.POST,instance=anomalie)
        if form.is_valid():
            anomalie = form.save()
            return redirect('anomalie',anomalie.id)
    else:
        form = EditAnomalieForm(instance=anomalie)

    return render(request,'suivi/editAnomalie.html',{'form':form,'anomalie':anomalie})

@login_required
@permission_required('suivi.change_budget', raise_exception = True)
def editBudget(request, id):
    budget = Budget.objects.get(id=id)

    if request.method == 'POST':
        form = EditBudgetForm(request.POST,instance = budget)
        if form.is_valid():
            budget = form.save()
            return redirect('affaire', budget.id_affaires.id)

    form = EditBudgetForm(instance = budget)

    return render(request,'suivi/editBudget.html', {'form':form, 'budget':budget})

@login_required
@permission_required('suivi.change_contact', raise_exception=True)
def editContact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        form = EditContactForm(request.POST, instance = contact)
        if form.is_valid():
            contact = form.save()
            return redirect('affaire', contact.id_affaires.id)
        
    form = EditContactForm(instance = contact)

    return render(request,'suivi/editContact.html', {'form':form, 'contact':contact})

@login_required
@permission_required('suivi.add_contact', raise_exception=True)
def createContact(request, id):
    affaire= Affaires.objects.get(id=id)

    if request.method == 'POST':
        form = EditContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.id_affaires = affaire
            form.save()

            return redirect('affaire', affaire.id)
        
    form = EditContactForm()

    return render(request,'suivi/createContact.html', {'form':form})

@login_required
@permission_required('suivi.change_avancementsousensemble', raise_exception=True)
def editAvancementSE(request, id):
    avancementSE = AvancementSousEnsemble.objects.get(id = id)
    sousEnsemble = SousEnsemble.objects.get(id = avancementSE.id_sousensemble.id)
    ensemble = Ensembles.objects.get(id = sousEnsemble.id_ensemble.id)
    avancementE = AvancementEnsemble.objects.get(id_ensembles = ensemble)

    if request.method == 'POST':
        form = EditAvancementSousEnsembleForm(request.POST, instance = avancementSE)
        
        if form.is_valid():
            avancementSE = form.save()
            avancements = AvancementSousEnsemble.objects.filter(id_ensemble = ensemble)
            dico = {"debit":0, "montage":0, "soudure":0, "ajustage_montage": 0, "peinture":0, "total":0}
            
            for i in avancements:
                if i.debit == 'EC':
                    dico["debit"] = dico["debit"] + 1
                if i.debit == 'TR':
                    dico["debit"] = dico["debit"] + 2

                if i.montage == 'EC':
                    dico["montage"] = dico["montage"] + 1
                if i.montage == 'TR':
                    dico["montage"] = dico["montage"] + 2

                if i.soudure == 'EC':
                    dico["soudure"] = dico["soudure"] + 1
                if i.soudure == 'TR':
                    dico["soudure"] = dico["soudure"] + 2

                if i.ajustage_montage == 'EC':
                    dico["ajustage_montage"] = dico["ajustage_montage"] + 1
                if i.ajustage_montage == 'TR':
                    dico["ajustage_montage"] = dico["ajustage_montage"] + 2

                if i.peinture == 'EC':
                    dico["peinture"] = dico["peinture"] + 1
                if i.peinture == 'TR':
                    dico["peinture"] = dico["peinture"] + 2

                dico["total"] = dico["total"] + 2

            avancementE.debit = int((dico["debit"] / dico["total"]) * 100)
            avancementE.montage = int((dico["montage"] / dico["total"]) * 100)
            avancementE.soudure = int((dico["soudure"] / dico["total"]) * 100)
            avancementE.ajustage_montage = int((dico["ajustage_montage"] / dico["total"]) * 100)
            avancementE.peinture = int((dico["peinture"] / dico["total"]) * 100)
            avancementE.avancement_global = int((dico["debit"] + dico["montage"] + dico["soudure"] + dico["ajustage_montage"] + dico["peinture"]) * 100 / (5 * dico["total"]))
            avancementE.save()
            
            return redirect('sousEnsemble', sousEnsemble.id)

    else:
        form = EditAvancementSousEnsembleForm(instance = avancementSE)

    return render(request, 'suivi/editAvancementSE.html', {'form':form, 'avancementSE':avancementSE, 'sousEnsemble':sousEnsemble})

@login_required
@permission_required('suivi.delete_affaires', raise_exception=True)
def deleteAffaire(request,id):
    affaire = Affaires.objects.get(id=id)

    if request.method == 'POST':
        affaire.delete()
        return redirect('rechercheAffaire')

    return render(request,'suivi/deleteAffaire.html',{'affaire':affaire})

@login_required
@permission_required('suivi.delete_outils', raise_exception=True)
def deleteOutil(request,id):
    outil = Outils.objects.get(id=id)
    affaire = outil.id_affaires

    if request.method == 'POST':
        outil.delete()
        return redirect('affaire', affaire.id)

    return render(request,'suivi/deleteOutil.html',{'outil':outil})

@login_required
@permission_required('suivi.delete_ensembles', raise_exception=True)
def deleteEnsemble(request,id):
    ensemble = Ensembles.objects.get(id = id)
    id_outil = ensemble.id_outils.id

    if request.method == 'POST':
        ensemble.delete()
        return redirect('outil', id_outil)

    return render(request,'suivi/deleteEnsemble.html',{'ensemble':ensemble})

@login_required
@permission_required('suivi.delete_sousensemble', raise_exception = True)
def deleteSousEnsemble(request,id):
    sousEnsemble = SousEnsemble.objects.get(id = id)
    ensemble = sousEnsemble.id_ensemble.id
    
    if request.method == 'POST':
        sousEnsemble.delete()
        return redirect('ensemble', ensemble)

    return render(request, 'suivi/deleteSousEnsemble.html', {'sousEnsemble':sousEnsemble})

@login_required
@permission_required('suivi.delete_pieces', raise_exception=True)
def deletePiece(request,id):
    piece = Pieces.objects.get(id = id)
    ensemble = piece.id_ensemble.id

    if request.method == 'POST':
        piece.delete()
        return redirect('ensemble',ensemble)

    return render(request,'suivi/deletePiece.html',{'piece':piece})

@login_required
@permission_required('suivi.delete_factures', raise_exception=True)
def deleteFacture(request,id):
    facture = Factures.objects.get(id=id)
    affaire = facture.id_affaire

    if request.method == 'POST':
        facture.delete()
        return redirect('affaire',affaire.id)

    return render(request,'suivi/deleteFacture.html',{'facture':facture,'affaire':affaire})

@login_required
@permission_required('suivi.delete_camions', raise_exception=True)
def deleteCamion(request,id):
    camion = Camions.objects.get(id=id)
    affaire = camion.id_affaires

    if request.method == 'POST':
        camion.delete()
        return redirect('affaire', affaire.id)

    return render(request,'suivi/deleteCamion.html',{'camion':camion})

@login_required
@permission_required('suivi.delete_chargementcamions', raise_exception=True)
def deleteChargementCamion(request,id):
    chargement = Chargementcamions.objects.get(id=id)
    camion = Camions.objects.get(id = chargement.id_camions.id)

    if request.method == 'POST':
        chargement.delete()
        return redirect('camion', camion.id)

    return render(request,'suivi/deleteChargementCamion.html',{'chargement':chargement, 'camion':camion})

@login_required
@permission_required('suivi.delete_commandes', raise_exception=True)
def deleteCommande(request,id):
    commande = Commandes.objects.get(id=id)
    affaire = commande.id_affaires

    if request.method == 'POST':
        commande.delete()
        return redirect('affaire', affaire.id)

    return render(request,'suivi/deleteCommande.html',{'commande':commande})

@login_required
@permission_required('suivi.delete_contact', raise_exception=True)
def deleteContact(request,id):
    contact = Contact.objects.get(id=id)
    affaire = contact.id_affaires

    if request.method == 'POST':
        contact.delete()
        return redirect('affaire',affaire.id)
    
    return render(request,'suivi/deleteContact.html',{'contact':contact})

class AffaireAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Affaires.objects.none()

        qs = Affaires.objects.all()

        if self.q:
            qs = qs.filter(numero__istartswith= self.q)

        return qs

    def get_result_label(self, result):
        return format_html('<p>{} - {}</p>', result.numero, result.chantier)

class FactureAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Factures.objects.none()

        qs = Factures.objects.all()

        if self.q:
            qs = qs.filter(numero__istartswith = self.q)

        return qs

    def get_result_label(self, result):
        return format_html('<p>{} - {}', result.numero, result.fournisseur)

class PieceEnsembleAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return PieceEnsemble.objects.none()

        qs = PieceEnsemble.objects.all().order_by('type','numero')

        affaire_id = self.forwarded.get('id_affaires',None)
        affaire = Affaires.objects.get(id = affaire_id)

        qs = qs.filter(id_affaires = affaire)

        if self.q:
            qs = qs.filter(numero__istartswith = self.q)

        return qs

    def get_result_label(self, result):

        return format_html('{} {} - {}', result.type, result.numero, result.nom)

class CommandeAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Commandes.objects.none()

        qs = Commandes.objects.all()

        if self.q:
            qs = qs.filter(numero__startswith = self.q)
        
        return qs

    def get_label_result(self, result):

        return format_html('{} {} - {}', result.numero, result.fournisseur, result.statut)

class FactureAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Factures.objects.none()

        qs = Factures.objects.all()

        if self.q:
            qs = qs.filter(numero__startswith = self.q)
        
        return qs

    def get_label_result(self,result):
        return format_html('{} - Affaire {}', result.numero, result.id_affaires.numero)

class CamionAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Camions.objects.none()

        qs = Camions.objects.all()

        if self.q:
            qs = qs.filter(identifiant__startswith = self.q)
        
        return qs

    def get_label_result(self,result):
        return format_html('{} {} - Affaire {}', result.identifiant, result.transporteur, result.id_affaires.numero)

class PieceEnsembleCamionAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return PieceEnsemble.objects.none()

        qs = PieceEnsemble.objects.all().order_by('type','numero')

        affaire_id = self.forwarded.get('id_affaires',None)
        affaire = Affaires.objects.get(id = affaire_id)

        qs = qs.filter(id_affaires = affaire)

        if self.q:
            qs = qs.filter(numero__startswith = self.q)

        return qs

    def get_label_result(self, result):
        return format_html('{} {} - {}', result.type, result.numero, result.nom)
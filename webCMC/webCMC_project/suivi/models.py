from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.

class Affaires(models.Model):
    numero = models.IntegerField(null=True)
    chantier = models.CharField(max_length=127)
    adresse_facturation = models.CharField(max_length=127)
    adresse_livraison_1 = models.CharField(max_length=127)
    adresse_livraison_2 = models.CharField(max_length=127)
    name_1 = models.CharField(max_length=127)
    name_2 = models.CharField(max_length=127)
    contact_1 = models.CharField(max_length=127)
    contact_2 = models.CharField(max_length=127)
    fabrication = models.CharField(max_length=16)
    budget_total = models.IntegerField(null=True)
    budget_matiere = models.IntegerField(null=True)
    budget_hydraulique = models.IntegerField(null=True)
    budget_mecanique = models.IntegerField(null=True)
    budget_heures = models.IntegerField(null=True)


class Outils(models.Model):
    numero = models.IntegerField(null=True)
    nom = models.CharField(max_length = 255, null=True)
    quantite = models.IntegerField(null=True)
    options = models.CharField(max_length=255)
    date_offre = models.CharField(max_length = 63, null=True)
    version_offre = models.CharField(max_length=127)
    lien_offre = models.CharField(max_length = 127, null=True)
    date_livraison = models.CharField(max_length = 63, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class Ensembles(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    poids = models.IntegerField(null=True)
    taux_de_complexite = models.IntegerField(null=True)
    miniature = models.CharField(max_length=127, null=True)
    couleur_peinture = models.CharField(max_length=127, null=True)
    colisage = models.CharField(max_length=127, null=True)
    livraison = models.CharField(max_length=127, null=True)
    nb_anomalies = models.IntegerField(null=True)
    budget_fab = models.IntegerField(null=True)
    reference = models.CharField(max_length=127, null=True)
    id_outils = models.ForeignKey(Outils, on_delete=models.CASCADE, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE, null=True)

class SousEnsemble(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    cout_unitaire = models.IntegerField(null = True, default=0)
    quantite = models.IntegerField(null = True, default = 0)
    poids = models.IntegerField(null=True, default = 0)
    indice_de_complexite = models.CharField(max_length=63, null = True)
    heures_fabrication = models.IntegerField(null = True, default = 0)
    plan = models.CharField(max_length=127, null=True)
    compagnon = models.CharField(max_length=127, null=True)
    nesting = models.CharField(max_length=127, null=True)
    feuilles_de_debit = models.CharField(max_length=127, null=True)
    couleur_peinture = models.CharField(max_length=127, null=True)
    colisage = models.CharField(max_length=127, null=True)
    of = models.CharField(max_length = 63, null=True)
    revision = models.IntegerField(null=True, default = 0)
    id_outils = models.ForeignKey(Outils, on_delete=models.CASCADE, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE, null=True)
    id_ensemble = models.ForeignKey(Ensembles,on_delete = models.CASCADE)
    

class Pieces(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    quantite = models.IntegerField(null=True, default = 0)
    poids_unitaire = models.IntegerField(null=True, default = 0)
    couleur = models.CharField(max_length=127)
    indice_complexite = models.IntegerField(null=True)
    heures_fabrication = models.IntegerField(null=True)
    cout_unitaire = models.CharField(max_length=63)
    of = models.CharField(max_length = 63, null=True)
    revision = models.IntegerField(null=True)
    plan = models.CharField(max_length=63, null = True)
    numero_ensemble = models.IntegerField(null=True)
    numero_outil = models.IntegerField(null=True)
    numero_affaire = models.IntegerField(null=True)
    id_ensemble = models.ForeignKey(Ensembles, on_delete=models.CASCADE)
    id_outil = models.ForeignKey(Outils, on_delete=models.CASCADE)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE, null = True)
    id_sous_ensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE, null=True)
    
class Nomenclature(models.Model):
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)
    id_outils = models.ForeignKey(Outils, on_delete=models.CASCADE, null=True)
    sous_projet = models.CharField(max_length=127,null=True)

class AvancementSousEnsemble(models.Model):
    NON_COMMENCE = '0'
    EN_COURS = 'EC'
    TERMINE = 'TR'
    ETAT_CHOIX= [
        (NON_COMMENCE, '0'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        ]

    numero_sousensemble = models.IntegerField(null=True)

    debit = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    montage = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    soudure = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    ajustage_montage = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    peinture = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    decoupe_cn = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    id_sousensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE)
    id_ensemble = models.ForeignKey(Ensembles, on_delete = models.CASCADE, null = True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class AvancementEnsemble(models.Model):
    debit = models.CharField(max_length=16, null=True)
    montage = models.CharField(max_length=16, null=True)
    soudure = models.CharField(max_length=16, null=True)
    ajustage_montage = models.CharField(max_length=16, null=True)
    peinture = models.CharField(max_length=16, null=True)
    avancement_global = models.CharField(max_length=16, null=True)
    id_ensembles = models.ForeignKey(Ensembles, on_delete=models.CASCADE)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class Camions(models.Model):
    identifiant = models.IntegerField(null=True)
    poids = models.IntegerField(null=True, default=0)
    transporteur = models.CharField(max_length=63, null=True)
    date_livraison = models.CharField(max_length=63,null=True, default= datetime.now().date())
    date_depart = models.CharField(max_length=63,null=True, default= datetime.now().date())
    photos = models.CharField(max_length=128,null=True)
    capacite = models.IntegerField(null=True, default=0)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE, null = True)

class Chargementcamions(models.Model):
    identifiant_camion = models.IntegerField(null=True)
    numero_piece = models.IntegerField(null=True)
    quantite_piece = models.IntegerField(null=True, default=1)
    poids_total = models.IntegerField(null=True, default=0)
    id_camions = models.ForeignKey(Camions, on_delete=models.CASCADE, null = True)
    id_pieces = models.ForeignKey(Pieces, on_delete=models.CASCADE,null = True)
    id_sous_ensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE, null = True)

class Commandes(models.Model):
    numero = models.IntegerField(null=True)
    fournisseur = models.CharField(max_length=127)
    devis = models.CharField(max_length=128,null=True)
    date_commande = models.CharField(max_length=63,null=True, default=datetime.now().date())
    date_reception = models.CharField(max_length=63,null=True, default=datetime.now().date())
    statut = models.CharField(max_length=127)
    id_affaires = models.ForeignKey(Affaires,null = True, on_delete=CASCADE)
    paired_commandes = models.ManyToManyField('self',symmetrical=True)

class Factures(models.Model):
    numero = models.IntegerField(null=True)
    fournisseur = models.CharField(max_length=127)
    type = models.CharField(max_length=127)
    facture = models.CharField(max_length=127,null=True)
    montant = models.CharField(max_length=127)
    attribution_budget = models.CharField(max_length=127)
    id_affaires = models.ForeignKey(Affaires, null= True, on_delete=CASCADE)
    paired_factures = models.ManyToManyField('self', symmetrical=True)

class Anomalies(models.Model):
    type= {'conception','fabrication'}
    description = models.CharField(max_length=511)
    etat = {'traitee','non traitee'}
    solution = models.CharField(max_length=255,null=True)
    commentaire = models.CharField(max_length=255,null=True)
    version = models.CharField(max_length=127,null=True)
   
class BudgetFabrication(models.Model):
    id_affaires = models.ForeignKey(Affaires, on_delete= models.CASCADE)
    type = {'AV','Revu initial','Révisé'}
    heures_debit = models.IntegerField(null=True)
    heures_montage = models.IntegerField(null=True)
    heures_soudage = models.IntegerField(null=True)
    heures_ajustage = models.IntegerField(null=True)

class MontageMecanoSoude(models.Model):
    Compagnon = models.CharField(max_length=127,null=True)
    date_debut = models.CharField(max_length=63,null=True)
    heures_consommees = models.IntegerField(null=True)
    date_fin = models.CharField(max_length=63,null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class Composants(models.Model):
    Type = models.CharField(max_length=127,null=True)
    besoin = models.CharField(max_length=127,null=True)
    devis = models.CharField(max_length=127,null=True)
    bon_commande = models.CharField(max_length=127,null=True)
    bon_livraison = models.CharField(max_length=127,null=True)
    reliquat = models.CharField(max_length=127,null=True)
    facture_fournisseur = models.CharField(max_length=127,null=True)

class Budget(models.Model):
    budget_matiere = models.IntegerField(default = 0)
    budget_hydraulique = models.IntegerField(default = 0)
    budget_mecanique = models.IntegerField(default = 0)
    budget_heures = models.IntegerField(default = 0)
    budget_total = models.IntegerField(default = 0)
    lieu_fab = models.IntegerField(null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE, null = True)

class PieceEnsemble(models.Model):
    numero = models.IntegerField(null=True)
    nom = models.CharField(max_length=63, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE)
    id_piece = models.ForeignKey(Pieces, on_delete=models.CASCADE, null=True)
    id_ensemble = models.ForeignKey(Ensembles, on_delete=models.CASCADE, null=True)
    id_sousensemble = models.ForeignKey(SousEnsemble, on_delete = models.CASCADE, null = True)
    type = models.CharField(max_length=63, null = True)

class Contact(models.Model):
    name = models.CharField(max_length=63,null=True)
    telephone = models.CharField(max_length=63, null=True)
    email = models.CharField(max_length=63, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE)
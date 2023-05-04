from django import forms
from dal import autocomplete
from suivi.models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.PasswordInput

class SearchAffaireForm(forms.ModelForm):
    class Meta:
        model = Affaires
        fields = ['numero']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'affaireAutocomplete',
                attrs={'data-html':True}
                )
            }

class SearchPieceForm(forms.ModelForm):
    class Meta:
        model = PieceEnsemble
        fields = ['numero', 'id_affaires']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'pieceEnsembleAutocomplete',
                forward = ('id_affaires',),
                attrs = {'data-html':True}
                ),
            'id_affaires': forms.HiddenInput()
            }

class SearchCommandeForm(forms.ModelForm):
    class Meta:
        model = Commandes
        fields = ['numero']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'commandeAutocomplete',
                attrs = {'data-html':True}
            ),
        }

class SearchFactureForm(forms.ModelForm):
    class Meta:
        model = Factures
        fields = ['numero']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'factureAutotcomplete',
                attrs = {'data-html':True}
            ),
        }

class SearchCamionForm(forms.ModelForm):
    class Meta:
        model = Camions
        fields= ['identifiant']
        widgets = {
            'identifiant': autocomplete.ListSelect2(
                url = 'camionAutocomplete',
                attrs = {'data-html':True}
            ),
        }

class SearchPieceEnsembleCamionForm(forms.ModelForm):
    class Meta:
        model = PieceEnsemble
        fields = ['numero', 'id_affaires']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'pieceEnsembleAutocomplete',
                forward = ('id_affaires',),
                attrs = {'data-html':True}
                ),
            'id_affaires': forms.HiddenInput()
            }

class CreatePieceEnsembleForm(forms.ModelForm):
    class Meta:
        model = PieceEnsemble
        exclude = ['id_affaires', 'id_piece', 'id_ensemble', 'type']

class RechercheCamionForm(forms.Form):
    numero = forms.IntegerField()

class RechercheFactureForm(forms.ModelForm):
    class Meta:
        model = Factures
        fields = ['numero']
        widgets = {
            'numero': autocomplete.ListSelect2(
                url = 'factureAutocomplete',
                attrs = {'data-html':True}
            )
        }

class RechercheCommandeForm(forms.ModelForm):
    class Meta:
        model = Commandes
        exclude = ['devis','date_commande','date_reception']

class RechercherCompagnonForm(forms.ModelForm):
    class Meta:
        model= Compagnon
        fields = ['nom']
        widgets = {
            'nom':autocomplete.ListSelect2(
                url = 'compagnonAutocomplete',
                attrs = {'data-html':True}
            )
        }

class PieceSearchForm(forms.Form):
    numero = forms.IntegerField()

class EditAffaireForm(forms.ModelForm):
    class Meta:
        model = Affaires
        fields = '__all__'

class CreateAffaireForm(forms.Form):
    class Meta:
        model = Affaires
        fields = ['numero','chantier']

class EditOutilForm(forms.ModelForm):
    class Meta:
        model = Outils
        exclude = ['id_affaires','numero_affaire']

class EditEnsembleForm(forms.ModelForm):
    class Meta:
        model = Ensembles
        exclude = ['id_affaires','id_outils','miniature','id_avancement']

class CreateEnsembleForm(forms.ModelForm):
    class Meta:
        model = Ensembles
        fields = ['nom','numero','poids','budget_fab']

class EditPieceForm(forms.ModelForm):
    class Meta:
        model = Pieces
        exclude = ['id_affaires','id_outil','id_ensemble','numero_affaire','numero_outil','numero_ensemble','id_sous_ensemble','id_avancement']

class EditCamionForm(forms.ModelForm):
    class Meta:
        model = Camions
        exclude = ['id_affaires']

class CreateCamionForm(forms.ModelForm):
    class Meta:
        model = Camions
        exclude = ['id_affaires','photos']

class EditFactureForm(forms.ModelForm):
    class Meta:
        model = Factures
        exclude = ['id_affaires', 'photos']
    
class EditChargementCamionForm(forms.ModelForm):
    class Meta:
        model = Chargementcamions
        exclude = ['id_camions','id_pieces','id_affaires','id_sous_ensemble', 'poids_total']

class EditCommandeForm(forms.ModelForm):
    class Meta:
        model = Commandes
        exclude = ['id_affaires']

class EditNomenclatureForm(forms.ModelForm):
    class Meta:
        model = Nomenclature
        exclude = ['id_affaires', 'id_outils']

class EditAnomalieForm(forms.ModelForm):
    class Meta:
        model = Anomalies
        fields = '__all__'

class AddChargementCamionForm(forms.ModelForm):
    class Meta:
        model = Chargementcamions
        exclude = ['id_camions','id_pieces','id_affaires','poids_total','identifiant_camion']

class CreateAvancementPieceForm(forms.ModelForm):
    class Meta:
        model = AvancementPiece
        exclude = ['id_piece','id_sous_ensemble']

class EditAvancementPieceForm(forms.ModelForm):
    class Meta:
        model = AvancementPiece
        exclude = ['id_piece','id_sous_ensemble','avancement_global']

class CreateAvancementSousEnsembleForm(forms.ModelForm):
    class Meta:
        model = AvancementSousEnsemble
        exclude = ['id_sousensemble','numero_sousensemble','id_affaires']

class EditAvancementSousEnsembleForm(forms.ModelForm):
    class Meta:
        model = AvancementSousEnsemble
        exclude = ['id_sousensemble','numero_sousensemble','id_affaires','id_ensemble','avancement_global']

class CreateAvancementEnsembleForm(forms.ModelForm):
    class Meta:
        model = AvancementSousEnsemble
        exclude = ['id_ensemble','numero_ensemble','id_affaires','id_nomenclature']

class EditAvancementEnsembleForm(forms.ModelForm):
    class Meta:
        model = AvancementSousEnsemble
        exclude = ['id_ensemble','numero_ensemble','id_affaires','avancement_global']

class EditDebitScieForm(forms.ModelForm):
    class Meta:
        model = DebitScie
        exclude = ['id_piece']

class EditDebitLaserForm(forms.ModelForm):
    class Meta:
        model = DebitLaser
        exclude = ['id_piece']

class EditTacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        exclude = ['id_piece','id_sous_ensemble','id_ensemble','id_affaire']

class EditBudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        exclude = ['id_affaires']

class CreateSousEnsembleForm(forms.ModelForm):
    class Meta:
        model = SousEnsemble
        fields = ['nom', 'numero']

class EditSousEnsembleForm(forms.ModelForm):
    class Meta:
        model = SousEnsemble
        exclude = ['id_affaires','id_outils','id_ensemble','id_avancement']

class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
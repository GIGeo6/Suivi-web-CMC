from django.contrib import admin

from suivi.models import *
# Register your models here.

class AffairesAdmin(admin.ModelAdmin):
    list_display = ('numero','chantier', 'id')

class OutilsAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'id_affaires')

class EnsemblesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'id_affaires')

class SousEnsemblesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'id_affaires')

class PiecesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'id_affaires')

class PieceEnsembleAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom','type', 'id_affaires', 'id_piece', 'id_ensemble')

class AvancementEnsembleAdmin(admin.ModelAdmin):
    list_display = ('id_affaires', 'id_ensembles', 'debitCN')

class AvancementSousEnsembleAdmin(admin.ModelAdmin):
    list_display = ('id_affaires','id_ensemble','id_sousensemble','numero_sousensemble')

class AvancementPieceAdmin(admin.ModelAdmin):
    list_display = ('id_sous_ensemble','id_piece','debitCn')

class NomenclatureAdmin(admin.ModelAdmin):
    list_display = ('sous_projet', 'id_outils', 'id_affaires')

class CamionsAdmin(admin.ModelAdmin):
    list_display = ('identifiant', 'transporteur')

class FacturesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fournisseur')

class CommandesAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fournisseur')

class ChargementCamionAdmin(admin.ModelAdmin):
    list_display = ('identifiant_camion','numero_piece')

class CompagnonAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','temps_hebdo')

class QualificationsAdmin(admin.ModelAdmin):
    list_display = ('compagnon','qualification','categorie')

class TacheAdmin(admin.ModelAdmin):
    list_display = ('id_affaire','id_piece','etat')

class DebitScieAdmin(admin.ModelAdmin):
    list_display = ('id_piece','type_profile','etat')

class DebitLaserAdmin(admin.ModelAdmin):
    list_display = ('id_piece','epaisseur','grade','etat')

admin.site.register(Affaires,AffairesAdmin)
admin.site.register(PieceEnsemble, PieceEnsembleAdmin)
admin.site.register(Outils, OutilsAdmin)
admin.site.register(Ensembles, EnsemblesAdmin)
admin.site.register(SousEnsemble, SousEnsemblesAdmin)
admin.site.register(Pieces, PiecesAdmin)
admin.site.register(AvancementEnsemble, AvancementEnsembleAdmin)
admin.site.register(AvancementSousEnsemble, AvancementSousEnsembleAdmin)
admin.site.register(AvancementPiece,AvancementPieceAdmin)
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Camions, CamionsAdmin)
admin.site.register(Factures, FacturesAdmin)
admin.site.register(Commandes, CommandesAdmin)
admin.site.register(Chargementcamions, ChargementCamionAdmin)
admin.site.register(Compagnon,CompagnonAdmin)
admin.site.register(Qualification,QualificationsAdmin)
admin.site.register(Tache,TacheAdmin)
admin.site.register(DebitScie,DebitScieAdmin)
admin.site.register(DebitLaser,DebitLaserAdmin)

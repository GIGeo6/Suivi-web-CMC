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
    list_display = ('id_affaires', 'id_ensembles', 'debit', 'montage')

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

admin.site.register(Affaires,AffairesAdmin)
admin.site.register(PieceEnsemble, PieceEnsembleAdmin)
admin.site.register(Outils, OutilsAdmin)
admin.site.register(Ensembles, EnsemblesAdmin)
admin.site.register(SousEnsemble, SousEnsemblesAdmin)
admin.site.register(Pieces, PiecesAdmin)
admin.site.register(AvancementEnsemble, AvancementEnsembleAdmin)
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(Camions, CamionsAdmin)
admin.site.register(Factures, FacturesAdmin)
admin.site.register(Commandes, CommandesAdmin)
admin.site.register(Chargementcamions, ChargementCamionAdmin)
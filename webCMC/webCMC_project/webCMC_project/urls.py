"""webCMC_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.conf import settings, urls
from django.contrib import admin
from django.urls import path,include
import suivi.views as suivi
#from suivi.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('suivi/', include('suivi.urls')),
    path('admin/', admin.site.urls),
    path('', suivi.index, name='index'),

    path('static/', static),
    

    path('suivi/login_view/', suivi.login_view, name='login_view'),
    path('suivi/affairesautocomplete/', suivi.AffaireAutocomplete.as_view(), name='affaireAutocomplete' ),
    path('suivi/factureAutocomplete/', suivi.FactureAutocomplete.as_view(), name='factureAutocomplete'),
    path('suivi/pieceEnsembleAutocomplete/', suivi.PieceEnsembleAutocomplete.as_view(), name ='pieceEnsembleAutocomplete'),
    path('suivi/commandeAutocomplete/', suivi.CommandeAutocomplete.as_view(), name = 'commandeAutocomplete'),
    path('suivi/camionAutocomplete/', suivi.CamionAutoComplete.as_view(), name='camionAutocomplete'),
    path('suivi/pieceEnsembleCamionAutocomplete/', suivi.PieceEnsembleCamionAutoComplete.as_view(), name='pieceEnsembleCamionAutocomplete'),

    path('suivi/affaire/<int:id>/', suivi.affaire, name='affaire'),
    path('suivi/outil/<int:id>/', suivi.outil, name='outil'),
    path('suivi/ensemble/<int:id>/', suivi.ensemble, name='ensemble'),
    path('suivi/sousEnsemble/<int:id>/', suivi.sousEnsemble, name='sousEnsemble'),
    path('suivi/piece/<int:id>/', suivi.piece, name='piece'),
    path('suivi/commande/<int:id>/', suivi.commande, name='commande'),
    path('suivi/nomenclature/<int:id>/', suivi.nomenclature, name='nomenclature'),
    path('suivi/facture/<int:id>/', suivi.facture, name='facture'),
    path('suivi/camion/<int:id>/', suivi.camion, name='camion'),

    path('suivi/editAffaire/<int:id>/', suivi.editAffaire, name='editAffaire'),
    path('suivi/editOutil/<int:id>/', suivi.editOutil, name='editOutil'),
    path('suivi/editEnsemble/<int:id>/', suivi.editEnsemble, name='editEnsemble'),
    path('suivi/editSousEnsemble/<int:id>/', suivi.editSousEnsemble, name='editSousEnsemble'),
    path('suivi/editPiece/<int:id>/', suivi.editPiece, name='editPiece'),
    path('suivi/editAnomalie/<int:id>/', suivi.editAnomalie, name='editAnomalie'),
    path('suivi/editNomenclature/<int:id>/', suivi.editNomenclature, name='editNomenclature'),
    path('suivi/editCamion/<int:id>/', suivi.editCamion, name='editCamion'),
    path('suivi/editFacture/<int:id>/', suivi.editFacture, name='editFacture'),
    path('suivi/editCommande/<int:id>/', suivi.editCommande, name='editCommande'),
    path('suivi/editBudget/<int:id>/', suivi.editBudget, name='editBudget'),
    path('suivi/editAvancementSE/<int:id>', suivi.editAvancementSE, name='editAvancementSE'),
    path('suivi/editChargementCamion/<int:id>', suivi.editChargementCamion, name="editChargementCamion"),

    path('suivi/lierCommande/<int:id>', suivi.lierCommande, name='lierCommande'),
    path('suivi/lierFacture/<int:id>', suivi.lierFacture, name='lierFacture'),

    path('suivi/rechercheAffaire/', suivi.rechercheAffaire, name='rechercheAffaire'),
    path('suivi/rechercheCamion/', suivi.rechercheCamion, name='rechercheCamion'),
    path('suivi/rechercheFacture/', suivi.rechercheFacture, name='rechercheFacture'),
    path('suivi/rechercheCommande/', suivi.rechercheCommande, name='rechercheCommande'),

    path('suivi/createAffaire/', suivi.createAffaire, name='createAffaire'),
    path('suivi/createAnomalie/', suivi.createAnomalie, name='createAnomalie'),
    path('suivi/createCamion/<int:id_affaire>/', suivi.createCamion, name='createCamion'),
    path('suivi/createCommande/<int:id_affaires>/', suivi.createCommande, name='createCommande'),
    path('suivi/createEnsemble/<int:id_affaire>/<int:id_outil>/', suivi.createEnsemble, name='createEnsemble'),
    path('suivi/createFacture/<int:id_affaire>/', suivi.createFacture, name='createFacture'),
    path('suivi/createNomenclature/<int:id_affaire>/<int:id_outil>/', suivi.createNomenclature, name='createNomenclature'),
    path('suivi/createPiece/<int:id_sousEnsemble>/', suivi.createPiece, name='createPiece'),
    path('suivi/createOutil/<int:id_affaires>/', suivi.createOutil, name='createOutil'),
    path('suivi/createSousEnsemble/<int:id_ensembles>/', suivi.createSousEnsemble, name='createSousEnsemble'),

    path('suivi/deleteAffaire/<int:id>/', suivi.deleteAffaire, name='deleteAffaire'),
    path('suivi/deleteOutil/<int:id>/', suivi.deleteOutil, name='deleteOutil'),
    path('suivi/deleteEnsemble/<int:id>/', suivi.deleteEnsemble, name='deleteEnsemble'),
    path('suivi/deleteSousEnsemble/<int:id>/', suivi.deleteSousEnsemble, name='deleteSousEnsemble'),
    path('suivi/deletePiece/<int:id>/', suivi.deletePiece, name='deletePiece'),
    path('suivi/deleteFacture/<int:id>/', suivi.deleteFacture, name='deleteFacture'),
    path('suivi/deleteCamion/<int:id>/', suivi.deleteCamion, name='deleteCamion'),
    path('suivi/deleteCommande/<int:id>/', suivi.deleteCommande, name='deleteCommande'),
    path('suivi/deleteChargementCamion/<int:id>', suivi.deleteChargementCamion, name='deleteChargementCamion'),
]


from . import views
from django.urls import path,include

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),

    path('affaire/<int:id>/', views.affaire, name='affaire'),
    path('outil/<int:id>/', views.outil, name='outil'),
    path('ensemble/<int:id>/', views.ensemble, name='ensemble'),
    path('piece/<int:id>/', views.piece, name='piece'),
    path('commande/<int:id>/', views.commande, name='commande'),
    path('suivi/nomenclature/<int:id>/', views.nomenclature, name='nomenclature'),
    path('suivi/ensembleAvancement/<int:id>/', views.ensembleCrea, name='ensembleAvancement'),
    path('suivi/ensembleCrea/<int:id>/', views.ensembleCrea, name='ensembleCrea'),
    path('suivi/ensemblePrepa/<int:id>/', views.ensembleCrea, name='ensemblePrepa'),

    path('editAffaire/<int:id>/', views.editAffaire, name='editAffaire'),
    path('editOutil/<int:id>/', views.editOutil, name='editOutil'),
    path('editEnsemble/<int:id>/', views.editEnsemble, name='editEnsemble'),
    path('editPiece/<int:id>/', views.editPiece, name='editPiece'),
    path('editAnomalie/<int:id>/', views.editAnomalie, name='editAnomalie'),
    path('editNomenclature/<int:id>/', views.editNomenclature, name='editNomenclature'),
    path('editCamion/<int:id>/', views.editCamion, name='editCamion'),
    path('editFacture/<int:id>/', views.editFacture, name='editFacture'),
    path('editCommande/<int:id>/', views.editCommande, name='editCommande'),
    path('editContact/<int:id>/', views.editContact, name='editContact'),

    path('rechercheAffaire/', views.rechercheAffaire, name='rechercheAffaire'),
    path('rechercheCamion/', views.rechercheCamion, name='rechercheCamion'),
    path('rechercheFacture/', views.rechercheFacture, name='rechercheFacture'),
    path('rechercheCommande/', views.rechercheCommande, name='rechercheCommande'),

    path('createAffaire/', views.createAffaire, name='createAffaire'),
    path('createAnomalie/', views.createAnomalie, name='createAnomalie'),
    path('createCamion/<int:id_affaire>', views.createCamion, name='createCamion'),
    path('createcommande/', views.createCommande, name='createCommande'),
    path('createEnsemble/<int:id_affaire>/<int:id_outil>', views.createEnsemble, name='createEnsemble'),
    path('createFacture/<int:id_ffaire>', views.createFacture, name='createFacture'),
    path('createNomenclature/', views.createNomenclature, name='createNomenclature'),
    path('createPiece/<int:id_affaire>/<int:id_outil>/<int:id_ensemble>', views.createPiece, name='createPiece'),
    path('createOutil/<int:id_affaires>', views.createOutil, name='createOutil'),
    path('createContact/<int:id_affaires>', views.createContact, name='createContact'),

    path('deleteAffaire/<int:id>', views.deleteAffaire, name='deleteAffaire'),
    path('deleteOutil/<int:id>', views.deleteOutil, name='deleteOutil'),
    path('deleteEnsemble/<int:id>', views.deleteEnsemble, name='deleteEnsemble'),
    path('deletePiece/<int:id>', views.deletePiece, name='deletePiece'),
    path('deleteFacture/<int:id>', views.deleteFacture, name='deleteFacture'),
    path('deleteCamion/<int:id>', views.deleteCamion, name='deleteCamion'),
    path('deleteContact/<int:id>', views.deleteContact, name='deleteContact'),
]
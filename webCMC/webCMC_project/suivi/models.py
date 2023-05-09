from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from datetime import datetime
import os
from django.dispatch import receiver

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

class Outils(models.Model):
    numero = models.IntegerField(null=True)
    nom = models.CharField(max_length = 255, null=True)
    quantite = models.IntegerField(null=True)
    lien_offre = models.CharField(max_length = 127, null=True)
    date_livraison = models.CharField(max_length = 63, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)
    fabrication = models.CharField(max_length=32, null=True)
    budget_total = models.IntegerField(default = 0, null=False)
    budget_matiere = models.IntegerField(default=0, null=False)
    budget_hydraulique = models.IntegerField(default=0, null=False)
    budget_mecanique = models.IntegerField(default=0, null=False)
    budget_heures = models.IntegerField(default=0, null=False)
    sym = models.IntegerField(default=0, null=False)
    image_outil = models.ImageField(upload_to='img/', null=True)

class Ensembles(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    poids = models.IntegerField(null=True)
    quantite = models.IntegerField(default=1, null=False)
    taux_de_complexite = models.IntegerField(null=True)
    miniature = models.CharField(max_length=127, null=True)
    couleur_peinture = models.CharField(max_length=127, null=True)
    colisage = models.CharField(max_length=127, null=True)
    livraison = models.CharField(max_length=127, null=True)
    nb_anomalies = models.IntegerField(null=True)
    budget_fab = models.IntegerField(null=True)
    reference = models.CharField(max_length=127, null=True)
    sym = models.IntegerField(default=0, null=False)
    id_avancement = models.ForeignKey('AvancementEnsemble', on_delete=models.CASCADE, null=True)
    id_outils = models.ForeignKey(Outils, on_delete=models.CASCADE, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE, null=True)
    image_ensemble = models.ImageField(upload_to='img/', null=True)

class SousEnsemble(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    cout_unitaire = models.IntegerField(null = True, default=0)
    quantite = models.IntegerField(null = True, default = 0)
    sym = models.IntegerField(default=0, null=False)
    poids = models.IntegerField(null=True, default = 0)
    indice_de_complexite = models.CharField(max_length=63, null = True)
    heures_fabrication = models.IntegerField(null = True, default = 0)
    heures_soudure= models.IntegerField(default=0, null=False)
    plan = models.CharField(max_length=127, null=True)
    compagnon = models.CharField(max_length=127, null=True)
    nesting = models.CharField(max_length=127, null=True)
    feuilles_de_debit = models.CharField(max_length=127, null=True)
    couleur_peinture = models.CharField(max_length=127, null=True)
    colisage = models.CharField(max_length=127, null=True)
    of = models.CharField(max_length = 63, null=True)
    revision = models.IntegerField(null=True, default = 0)
    id_avancement = models.ForeignKey('AvancementSousEnsemble', on_delete=models.CASCADE, null=True)
    id_outils = models.ForeignKey(Outils, on_delete=models.CASCADE, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE, null=True)
    id_ensemble = models.ForeignKey(Ensembles,on_delete = models.CASCADE)
    image_sous_ensemble = models.ImageField(upload_to='img/', null=True)
    

class Pieces(models.Model):
    nom = models.CharField(max_length=127)
    numero = models.IntegerField(null=True)
    quantite = models.IntegerField(null=False, default = 0)
    sym = models.IntegerField(default=0, null=False)
    poids_unitaire = models.IntegerField(null=True, default = 0)
    couleur = models.CharField(max_length=127)
    indice_complexite = models.IntegerField(null=True)
    heures_fabrication = models.IntegerField(null=True)
    heures_soudure = models.IntegerField(null=True)
    cout_unitaire = models.CharField(max_length=63)
    of = models.CharField(max_length = 63, null=True)
    revision = models.IntegerField(null=True)
    plan = models.CharField(max_length=63, null = True)
    numero_ensemble = models.IntegerField(null=True)
    numero_outil = models.IntegerField(null=True)
    numero_affaire = models.IntegerField(null=True)
    id_avancement = models.ForeignKey('AvancementPiece', on_delete=models.CASCADE, null=True)
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

    usinage = models.CharField(max_length=4, default=0)
    debitScie = models.CharField(max_length=4, default = 0)
    fabrication = models.CharField(max_length=4, default = 0)
    soudure = models.CharField(max_length=4, default = 0)
    ajustage_montage = models.CharField(max_length=4, default = 0)
    peinture = models.CharField(max_length=4, default = 0)
    debitCn = models.CharField(max_length=4, default = 0)
    livraison = models.BooleanField(default=False)
    avancement_global = models.CharField(max_length=16, null=True)
    id_sousensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE)
    id_ensemble = models.ForeignKey(Ensembles, on_delete = models.CASCADE, null = True)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class AvancementEnsemble(models.Model):
    
    usinage = models.CharField(max_length=16, default=0)
    debitScie = models.CharField(max_length=16, default = 0)
    debitCN = models.CharField(max_length=15, default = 0)
    montage = models.CharField(max_length=4, default = 0)
    soudure = models.CharField(max_length=16, default = 0)
    ajustage_montage = models.CharField(max_length=16, default = 0)
    peinture = models.CharField(max_length=16, default = 0)
    livraison = models.BooleanField(default=False)
    avancement_global = models.CharField(max_length=16, null=True)
    id_ensembles = models.ForeignKey(Ensembles, on_delete=models.CASCADE)
    id_affaires = models.ForeignKey(Affaires, on_delete=models.CASCADE)

class AvancementPiece(models.Model):
    NON_COMMENCE = '0'
    EN_COURS = 'EC'
    TERMINE = 'TR'
    ETAT_CHOIX= [
        (NON_COMMENCE, '0'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        ]
    
    FACILE = 'Facile'
    MOYEN = 'Moyen'
    DIFFICILE = 'Difficile'
    DIFFICULTE_CHOIX = [
        (FACILE,'Facile'),
        (MOYEN,'Moyen'),
        (DIFFICILE,'Difficile'),
        ]
    
    usinage = models.CharField(max_length=4, choices= ETAT_CHOIX, default = NON_COMMENCE)
    debitScie = models.CharField(max_length=4, choices = ETAT_CHOIX, default= NON_COMMENCE)
    debitCn = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    fabrication = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    soudure = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    ajustage_montage = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    peinture = models.CharField(max_length=4, choices = ETAT_CHOIX, default = NON_COMMENCE)
    type_tache = models.CharField(max_length=64, null = False)
    complexite = models.CharField(max_length=16, choices=DIFFICULTE_CHOIX, null=False)
    quantite = models.IntegerField(null=False,default=1)
    sym = models.IntegerField(null=False, default=0)
    temps_adapte = models.CharField(max_length=16, null=False, default=0)
    ratio = models.FloatField(max_length=16, null=False, default=1)
    livraison = models.BooleanField(default=False)
    avancement_global = models.CharField(max_length=16, null=True)
    id_sous_ensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE, null = False)
    id_piece = models.OneToOneField(Pieces,on_delete=models.CASCADE, null = False)

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

class CommandeAffaire(models.Model):
    id_affaire = models.ForeignKey(Affaires, on_delete=models.CASCADE, null=False)
    id_commande = models.ForeignKey(Commandes, on_delete=models.CASCADE, null=False)

class Factures(models.Model):
    numero = models.IntegerField(null=True)
    fournisseur = models.CharField(max_length=127)
    type = models.CharField(max_length=127)
    facture = models.CharField(max_length=127,null=True)
    montant = models.CharField(max_length=127)
    attribution_budget = models.CharField(max_length=127)

class FactureAffaire(models.Model):
    id_affaire = models.ForeignKey(Affaires, on_delete=models.CASCADE, null=False)
    id_facture = models.ForeignKey(Factures, on_delete=models.CASCADE, null=False)

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
    type = models.CharField(max_length=63, choices=[('piece','piece'),('sous-ensemble','sous-ensemble'),('ensemble','ensemble')], null = False, default='piece')

class Contact(models.Model):
    name = models.CharField(max_length=63,null=True)
    telephone = models.CharField(max_length=63, null=True)
    email = models.CharField(max_length=63, null=True)
    id_affaires = models.ForeignKey(Affaires, on_delete = models.CASCADE)

class Compagnon(models.Model):
    nom = models.CharField(max_length=63, null=False)
    prenom = models.CharField(max_length=63, null=False)
    temps_hebdo = models.IntegerField(null=False)

    def __str__(self):
        return self.nom

class Qualification(models.Model):

    PEINTRE = 1
    DEBITEUR = 2
    SOUDEUR = 3
    TRAPPEUR = 4
    CHAUDRONNIER = 5
    MONTEUR = 6
    QUALIFICATION_CHOIX= [
        (PEINTRE, 'Peintre'),
        (DEBITEUR, 'Débiteur'),
        (SOUDEUR, 'Soudeur'),
        (TRAPPEUR, 'Trappeur'),
        (CHAUDRONNIER, 'Chaudronnier'),
        (MONTEUR, 'Monteur'),
        ]
    
    P1='P1'
    P2='P2'
    P3='P3'
    NON='NON'
    CATEGORIE_CHOIX = [
        (NON,'Non'),
        (P1,'P1'),
        (P2,'P2'),
        (P3,'P3'),
    ]
    
    compagnon = models.ForeignKey(Compagnon, on_delete=models.CASCADE, null=False)
    qualification = models.IntegerField(choices = QUALIFICATION_CHOIX, default=0)
    categorie = models.CharField(max_length=63, choices = CATEGORIE_CHOIX, default=NON)

class Tache(models.Model):

    NON_COMMENCE = '0'
    EN_COURS = 'EC'
    TERMINE = 'TR'
    ETAT_CHOIX= [
        (NON_COMMENCE, '0'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        ]
    
    K = 'K'
    Q = 'Q'
    UNITE_CHOIX= [
        (K, 'kg'),
        (Q, 'Qte'),
    ]

    PEINTRE = '1'
    DEBITEUR = '2'
    SOUDEUR = '3'
    TRAPPEUR = '4'
    CHAUDRONNIER = '5'
    MONTEUR = '6'
    QUALIFICATION_CHOIX= [
        (PEINTRE, 'Peintre'),
        (DEBITEUR, 'Débiteur'),
        (SOUDEUR, 'Soudeur'),
        (TRAPPEUR, 'Trappeur'),
        (CHAUDRONNIER, 'Chaudronnier'),
        (MONTEUR, 'Monteur'),
        ]
    
    id_piece = models.ForeignKey(Pieces, on_delete=models.CASCADE, null=True)
    id_sous_ensemble = models.ForeignKey(SousEnsemble, on_delete=models.CASCADE, null=True)
    id_ensemble = models.ForeignKey(Ensembles, on_delete=models.CASCADE, null=True)
    id_compagnon = models.ForeignKey(Compagnon, on_delete=models.CASCADE, null=True)
    id_affaire = models.ForeignKey(Affaires, on_delete=models.CASCADE, null=False)
    temps_estime = models.IntegerField(default=0)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    etat = models.CharField(max_length=63, choices = ETAT_CHOIX, default=NON_COMMENCE)
    type = models.CharField(max_length=63, null=False)
    qualification = models.CharField(max_length = 15, choices = QUALIFICATION_CHOIX, default='0')
    unite = models.CharField(max_length=15, choices = UNITE_CHOIX, default=K)
    quantite = models.IntegerField(null=True)

class DebitScie(models.Model):

    NON_COMMENCE = '0'
    EN_COURS = 'EC'
    TERMINE = 'TR'
    ETAT_CHOIX= [
        (NON_COMMENCE, '0'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        ]
    
    id_piece = models.ForeignKey(Pieces, on_delete=models.CASCADE, null=False)
    type_profile = models.CharField(max_length=63, null=True)
    etat = models.CharField(max_length=63, choices = ETAT_CHOIX, default=NON_COMMENCE)

class DebitLaser(models.Model):

    NON_COMMENCE = '0'
    EN_COURS = 'EC'
    TERMINE = 'TR'
    ETAT_CHOIX= [
        (NON_COMMENCE, '0'),
        (EN_COURS, 'En cours'),
        (TERMINE, 'Terminé'),
        ]
    
    NON = 'Non'
    LARMEE = 'Larmée'
    QUATRE = '4'
    CINQ = '5'
    SIX = '6'
    HUIT = '8'
    DOUZE = '12'
    QUINZE = '15'
    VINGT = '20'

    EPAISSEUR_CHOIX = [
        (NON,'Non'),
        (LARMEE,'Larmée'),
        (QUATRE,'4'),
        (CINQ,'5'),
        (SIX,'6'),
        (HUIT,'8'),
        (DOUZE,'12'),
        (QUINZE,'15'),
        (VINGT,'20'),
        ]
    
    id_piece = models.ForeignKey(Pieces, on_delete = models.CASCADE, null = False)
    epaisseur = models.CharField(max_length=8, choices=EPAISSEUR_CHOIX, default = 'Non')
    grade = models.CharField(max_length=16, null = True)
    etat = models.CharField(max_length=63, choices = ETAT_CHOIX, default=NON_COMMENCE)


@receiver(models.signals.post_delete,sender=Outils)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image_outil.path):
            os.remove(instance.image_outil.path)

@receiver(models.signals.pre_save,sender=Outils)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_file = Outils.objects.get(pk=instance.pk).image_outil
    except Outils.DoesNotExist:
        return False
    
    new_file = instance.image_outil
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(models.signals.post_delete,sender=Ensembles)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image_ensemble.path):
            os.remove(instance.image_ensemble.path)

@receiver(models.signals.pre_save,sender=Ensembles)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_file = Ensembles.objects.get(pk=instance.pk).image_ensemble
    except Ensembles.DoesNotExist:
        return False
    
    new_file = instance.image_ensemble
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
            
@receiver(models.signals.post_delete,sender=SousEnsemble)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image_sous_ensemble.path):
            os.remove(instance.image_sous_ensemble.path)

@receiver(models.signals.pre_save,sender=SousEnsemble)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_file = SousEnsemble.objects.get(pk=instance.pk).image_sous_ensemble
    except SousEnsemble.DoesNotExist:
        return False
    
    new_file = instance.image_sous_ensemble
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
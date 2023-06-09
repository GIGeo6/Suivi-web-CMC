# Generated by Django 3.2.9 on 2022-01-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0008_remove_outils_numero_affaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='anomalies',
            name='commentaire',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='anomalies',
            name='solution',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='anomalies',
            name='version',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='avancement',
            name='numero_piece',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_heures',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_hydraulique',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_matiere',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_mecanique',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='lieu_fab',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budgetfabrication',
            name='heures_ajustage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budgetfabrication',
            name='heures_debit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budgetfabrication',
            name='heures_montage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budgetfabrication',
            name='heures_soudage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='capacite',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='date_depart',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='date_livraison',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='identifiant',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='photos',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='poids',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='camions',
            name='transporteur',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chargementcamions',
            name='identifiant_camion',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chargementcamions',
            name='numero_piece',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chargementcamions',
            name='poids_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chargementcamions',
            name='quantite_piece',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='Type',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='besoin',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='bon_commande',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='bon_livraison',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='devis',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='facture_fournisseur',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='composants',
            name='reliquat',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='factures',
            name='facture',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='factures',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='montagemecanosoude',
            name='Compagnon',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='montagemecanosoude',
            name='date_debut',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='montagemecanosoude',
            name='date_fin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='montagemecanosoude',
            name='heures_consommees',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='numero_affaire',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='sous_projet',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='heures_fabrication',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='indice_complexite',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='numero',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='numero_affaire',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='numero_ensemble',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='numero_outil',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='of',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='poids_unitaire',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='quantite',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pieces',
            name='revision',
            field=models.IntegerField(null=True),
        ),
    ]

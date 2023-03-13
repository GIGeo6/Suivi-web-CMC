# Generated by Django 3.2.9 on 2022-01-03 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chantier', models.CharField(max_length=127)),
                ('adresse_facturation', models.CharField(max_length=127)),
                ('adresse_livraison_1', models.CharField(max_length=127)),
                ('adresse_livraison_2', models.CharField(max_length=127)),
                ('name_1', models.CharField(max_length=127)),
                ('name_2', models.CharField(max_length=127)),
                ('contact_1', models.CharField(max_length=127)),
                ('contact_2', models.CharField(max_length=127)),
                ('fabrication', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Anomalies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='Avancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.affaires')),
            ],
        ),
        migrations.CreateModel(
            name='Camions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Chargementcamions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_affaires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.affaires')),
            ],
        ),
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fournisseur', models.CharField(max_length=127)),
                ('statut', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Ensembles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Factures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fournisseur', models.CharField(max_length=127)),
                ('type', models.CharField(max_length=127)),
                ('montant', models.CharField(max_length=127)),
                ('attribution_budget', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_affaires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.affaires')),
            ],
        ),
        migrations.CreateModel(
            name='Outils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=255)),
                ('version_offre', models.CharField(max_length=127)),
                ('id_affaires', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.affaires')),
            ],
        ),
        migrations.CreateModel(
            name='Pieces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('couleur', models.CharField(max_length=127)),
                ('cout_unitaire', models.CharField(max_length=63)),
                ('id_affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.affaires')),
                ('id_ensemble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.ensembles')),
                ('id_outil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.outils')),
            ],
        ),
        migrations.DeleteModel(
            name='Affaire',
        ),
        migrations.AddField(
            model_name='chargementcamions',
            name='id_pieces',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.pieces'),
        ),
        migrations.AddField(
            model_name='avancement',
            name='id_piece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.pieces'),
        ),
    ]

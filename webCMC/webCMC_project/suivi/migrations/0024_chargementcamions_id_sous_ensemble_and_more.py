# Generated by Django 4.0.2 on 2022-03-16 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0023_alter_camions_date_depart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargementcamions',
            name='id_sous_ensemble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suivi.sousensemble'),
        ),
        migrations.AlterField(
            model_name='chargementcamions',
            name='id_pieces',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suivi.pieces'),
        ),
    ]

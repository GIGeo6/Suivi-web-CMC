# Generated by Django 4.0.2 on 2022-03-16 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0022_alter_camions_capacite_alter_camions_date_depart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camions',
            name='date_depart',
            field=models.CharField(default=datetime.date(2022, 3, 16), max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='camions',
            name='date_livraison',
            field=models.CharField(default=datetime.date(2022, 3, 16), max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='commandes',
            name='date_commande',
            field=models.CharField(default=datetime.date(2022, 3, 16), max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='commandes',
            name='date_reception',
            field=models.CharField(default=datetime.date(2022, 3, 16), max_length=63, null=True),
        ),
    ]

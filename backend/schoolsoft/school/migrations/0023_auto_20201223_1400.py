# Generated by Django 3.1.4 on 2020-12-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20201223_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annee',
            name='is_actif',
            field=models.BooleanField(unique=True, verbose_name='Année en cours'),
        ),
    ]

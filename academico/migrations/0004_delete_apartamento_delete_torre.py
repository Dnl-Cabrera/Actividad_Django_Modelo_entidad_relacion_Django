# Generated by Django 4.2.1 on 2023-05-23 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_torre_id_domicilio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apartamento',
        ),
        migrations.DeleteModel(
            name='Torre',
        ),
    ]
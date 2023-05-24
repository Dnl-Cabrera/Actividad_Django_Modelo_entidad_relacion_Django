# Generated by Django 4.2.1 on 2023-05-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Torre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Carga_horaria',
        ),
    ]
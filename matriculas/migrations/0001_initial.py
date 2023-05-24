# Generated by Django 4.2.1 on 2023-05-23 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acudientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(default='', max_length=50, unique=True)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('telefono', models.CharField(default='', max_length=50)),
                ('estado_usuario', models.CharField(default='', max_length=50)),
                ('fecha_creacion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(default='', max_length=50, unique=True)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('telefono', models.CharField(default='', max_length=50)),
                ('estado_estudiante', models.CharField(default='', max_length=50)),
                ('fecha_creacion', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_matricula', models.CharField(default='', max_length=50)),
                ('fecha_matricula', models.CharField(default='', max_length=50)),
                ('id_acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculas.acudientes')),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculas.estudiantes')),
            ],
        ),
    ]
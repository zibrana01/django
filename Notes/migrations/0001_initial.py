# Generated by Django 4.2.6 on 2023-10-30 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=50)),
                ('date_naissance', models.DateField()),
                ('id_eleve', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=50)),
                ('date_naissance', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.FloatField(null=True)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.eleve')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=2, unique=True)),
                ('matiere', models.ManyToManyField(to='Notes.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='eleve',
            name='matiere',
            field=models.ManyToManyField(to='Notes.matiere'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.niveau'),
        ),
    ]
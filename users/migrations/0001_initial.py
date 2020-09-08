# Generated by Django 3.1.1 on 2020-09-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('username', models.CharField(max_length=100, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]

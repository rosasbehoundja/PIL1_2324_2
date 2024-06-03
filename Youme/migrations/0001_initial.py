# Generated by Django 4.2.13 on 2024-06-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('motdepasse', models.CharField(max_length=255)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-14 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youme', '0017_profile_hobbies_préférences_hobbies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2024, 6, 14, 18, 19, 40, 630756)),
        ),
    ]
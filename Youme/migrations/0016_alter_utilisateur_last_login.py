# Generated by Django 4.2.13 on 2024-06-13 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youme', '0015_alter_utilisateur_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2024, 6, 13, 2, 45, 18, 311564)),
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-19 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youme', '0029_discussion_message_remove_privateroom_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2024, 6, 19, 20, 58, 47, 462795)),
        ),
    ]
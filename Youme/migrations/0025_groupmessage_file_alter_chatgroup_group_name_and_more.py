# Generated by Django 4.2.13 on 2024-06-19 11:19

import datetime
from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('Youme', '0024_chatgroup_groupmessage_inboxmessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='body',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2024, 6, 19, 12, 19, 11, 760798)),
        ),
    ]
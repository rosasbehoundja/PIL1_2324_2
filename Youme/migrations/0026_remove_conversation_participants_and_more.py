# Generated by Django 4.2.13 on 2024-06-19 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youme', '0025_groupmessage_file_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='groupmessage',
            name='group',
        ),
        migrations.RemoveField(
            model_name='inboxmessage',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='inboxmessage',
            name='sender',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2024, 6, 19, 14, 12, 7, 965766)),
        ),
        migrations.DeleteModel(
            name='ChatGroup',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='GroupMessage',
        ),
        migrations.DeleteModel(
            name='InboxMessage',
        ),
    ]

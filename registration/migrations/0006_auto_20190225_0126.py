# Generated by Django 2.1.5 on 2019-02-25 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20190225_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='link',
        ),
    ]

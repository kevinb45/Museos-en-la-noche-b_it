# Generated by Django 2.1.5 on 2019-02-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
    ]
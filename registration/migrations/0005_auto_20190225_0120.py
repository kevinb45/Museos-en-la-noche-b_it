# Generated by Django 2.1.5 on 2019-02-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20190225_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono'),
        ),
    ]

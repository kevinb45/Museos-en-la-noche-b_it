# Generated by Django 2.1.7 on 2019-03-19 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0012_auto_20190319_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]

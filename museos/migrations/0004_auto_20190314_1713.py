# Generated by Django 2.1.5 on 2019-03-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_auto_20190314_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
    ]

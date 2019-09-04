# Generated by Django 2.1.7 on 2019-03-25 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0015_auto_20190325_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='close_hour',
            field=models.CharField(choices=[('00:00', 'Medianoche'), ('01:00', '01:00 AM'), ('02:00', '02:00 AM'), ('03:00', '03:00 AM'), ('04:00', '04:00 AM'), ('05:00', '05:00 AM'), ('06:00', '06:00 AM'), ('07:00', '07:00 AM'), ('08:00', '08:00 AM'), ('09:00', '09:00 AM'), ('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', 'Mediodia'), ('13:00', '01:00 PM'), ('14:00', '02:00 PM'), ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM'), ('18:00', '06:00 PM'), ('19:00', '07:00 PM'), ('20:00', '08:00 PM'), ('21:00', '09:00 PM'), ('22:00', '10:00 PM'), ('23:00', '11:00 PM')], max_length=20, verbose_name='Cierre'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='activities',
            field=models.ManyToManyField(blank=True, to='museos.Actividades', verbose_name='Lista de actividades'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='author',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
    ]

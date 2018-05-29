# Generated by Django 2.0.3 on 2018-05-22 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emisora', '0012_auto_20180521_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='fecha_final',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fin'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='programa',
            name='fecha_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Inicio'),
            preserve_default=False,
        ),
    ]
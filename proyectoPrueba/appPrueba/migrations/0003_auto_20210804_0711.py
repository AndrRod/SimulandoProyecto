# Generated by Django 3.2.3 on 2021-08-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrueba', '0002_alter_deudores_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='deudores',
            name='fecha_actualizacion_datos',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deudores',
            name='regularizo_situacion',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

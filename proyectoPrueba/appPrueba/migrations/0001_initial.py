# Generated by Django 3.2.3 on 2021-08-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deudores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('dni', models.IntegerField()),
                ('expediente', models.IntegerField(help_text='Ingresar solo cantidad de expedientes que está afectado')),
            ],
        ),
    ]

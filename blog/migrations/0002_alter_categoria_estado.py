# Generated by Django 4.1.1 on 2022-10-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activa/Inactiva'),
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-25 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '__first__'),
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.Unit'),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
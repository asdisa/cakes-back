# Generated by Django 2.1.3 on 2018-11-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='units',
            old_name='in_gramms',
            new_name='in_grams',
        ),
    ]
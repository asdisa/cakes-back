# Generated by Django 2.1.3 on 2018-12-01 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_container',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes.Image_container'),
        ),
    ]

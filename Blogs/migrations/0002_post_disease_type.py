# Generated by Django 5.0.6 on 2024-08-07 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
        ('MainApp', '0004_alter_diseaseinfo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='disease_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.diseaseinfo'),
        ),
    ]
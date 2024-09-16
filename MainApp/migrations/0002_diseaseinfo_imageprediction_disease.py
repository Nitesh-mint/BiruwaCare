# Generated by Django 5.0.6 on 2024-07-31 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(blank=True, upload_to='disease_thumbnail')),
                ('description', models.TextField()),
                ('category', models.CharField(help_text='Category of fruit or vegetable', max_length=100)),
                ('type', models.CharField(help_text='type of disease', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='imageprediction',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.diseaseinfo'),
        ),
    ]

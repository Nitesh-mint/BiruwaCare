# Generated by Django 5.0.6 on 2024-07-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_diseaseinfo_imageprediction_disease'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diseaseinfo',
            options={'verbose_name': 'DiseaseInfo', 'verbose_name_plural': 'DiseaseInfos'},
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='solution',
            field=models.TextField(null=True),
        ),
    ]
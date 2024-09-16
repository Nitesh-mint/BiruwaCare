import os
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
#for signals
from django.db.models.signals import post_delete
from django.dispatch import receiver

from accounts.models import CustomUser

class DiseaseInfo(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='disease_thumbnail', blank=True)
    description = CKEditor5Field('Text', config_name='extends', blank=True, null=True, help_text="description of disease")
    category = models.CharField(max_length=100, help_text="Category of fruit or vegetable")
    type = models.CharField(max_length=50, help_text="type of disease")
    solution = CKEditor5Field('Text', config_name='extends', blank=True, null=True, help_text="Solution of the disease")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "DiseaseInfo"
        verbose_name_plural = "DiseaseInfos"


#To delete thumbnail of the disease when the object is deleted
@receiver(post_delete, sender=DiseaseInfo)
def delete_thumbnail_on_delete(sender, instance, **kwargs):
    if instance.thumbnail and os.path.isfile(instance.thumbnail.path):
        os.remove(instance.thumbnail.path)

class ImagePrediction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Prediction_Image')
    prediction = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(DiseaseInfo,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.prediction


from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

from MainApp.models import DiseaseInfo

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to='post_thumbnail')
    body = CKEditor5Field('Text', config_name='extends')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    disease_type = models.ForeignKey(DiseaseInfo,on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])

from django.contrib import admin

from .models import ImagePrediction, DiseaseInfo

admin.site.register(ImagePrediction)
admin.site.register(DiseaseInfo)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.gis.db import models as gis_models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    image = models.ImageField(upload_to='Profile Picture', blank=True, null=True)
    location = gis_models.PointField(srid=4326, blank=True, null=True)

    def get_aboslute_url(self):
        return reverse('profile_detail', args=[str(self.id)])

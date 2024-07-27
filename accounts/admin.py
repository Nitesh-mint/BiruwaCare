from django.contrib import admin
import mapwidgets
from django.contrib.gis.db import models as gis_models

from .models import CustomUser

class AccountAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PointField: {"widget": mapwidgets.GoogleMapPointFieldWidget}
    }

admin.site.register(CustomUser, AccountAdmin)
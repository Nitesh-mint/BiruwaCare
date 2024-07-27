from django import forms
from mapwidgets.widgets import GoogleMapPointFieldWidget

from .models import CustomUser

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'image', 'location']
        widgets = {
            'location': GoogleMapPointFieldWidget,
        }
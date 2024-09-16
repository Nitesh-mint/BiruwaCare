from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from dotenv import load_dotenv
import os
load_dotenv()


from .models import CustomUser
from .forms import CustomUserUpdateForm
from MainApp.models import ImagePrediction, DiseaseInfo

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"
    context_object_name = 'user'

    def get_user(self):
        return self.request.user
    
    def get_user_location(self):
        user = self.get_user()
        if not user.location:
            return None, None, None
        
        lat = user.location[1]
        lon = user.location[0]
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={os.getenv("OPEN_WEATHER_API_KEY")}'
        cache_key = f'weather_data_{lat}_{lon}'
        data = cache.get(cache_key)
        if not data:
            try:
                response = requests.get(url)
                response.raise_for_status() #raise exception for http errors
                data = response.json()
                cache.set(cache_key, data, timeout=36000)
            except requests.RequestException as e:
                data = {}   
        weather_info = data.get('list', [])[0].get('weather', [])[0]
        city = data.get('city', {})
        weather_id = weather_info.get('id')
        city_id = city.get('id')
        city_name = city.get('name')
        return weather_id, city_id, city_name
    

    
    def get_user_prediction_history(self):
        user = self.get_user()
        user_predictions = ImagePrediction.objects.filter(user=user)[::-1]
        return user_predictions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_id, city_id , city_name = self.get_user_location()
        history = self.get_user_prediction_history()[:5]
        context = {
            'user': self.get_user(),
            'weather_id': weather_id,
            'city_id': city_id,
            'city_name': city_name,
            'history':history,
        }
        return context
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'account/User_update_view.html'

    def get_success_url(self):
        return reverse('profile')
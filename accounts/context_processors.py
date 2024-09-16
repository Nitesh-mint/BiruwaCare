from django.core.cache import cache
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_user_location(request):
        user = request.user
        appid = os.getenv("OPEN_WEATHER_API_KEY")
        if user.is_authenticated:
            try:
                lat = user.location[1]
                lon = user.location[0]
                url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={appid}'
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
                city = data.get('city', {})
                city_id = city.get('id')
                return {'city_id':city_id, 'appid':appid}
            except Exception:
                return {}
        return {}
from django.urls import path

from .views import home, predict, input_image

urlpatterns = [
    path('home/', home, name="home"),
    path('predict/', predict, name='predict'),
    path('send_image/', input_image, name='input_image'),
]

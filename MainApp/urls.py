from django.urls import path

from .views import home, predict,  upload_image, result

urlpatterns = [
    path('', home, name="home"),
    path('predict/', predict, name='predict'),
    path('upload_image/', upload_image, name='upload_image'),
    path('result/<int:pk>/', result, name="result"),
]

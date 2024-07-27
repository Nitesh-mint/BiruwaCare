from django.urls import path

from .views import ProfileView, ProfileUpdateView
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('UpdateProfile/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
]
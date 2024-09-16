"""
URL configuration for BiruwaCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))J
"""
from django.conf import settings # for static to work
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # for staticfiles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("MainApp.urls")),
    path('accounts/', include('accounts.urls')),
    path('blogs/',include("Blogs.urls")),
    #CKEditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    #For allauth
    path('accounts/', include("allauth.urls")),
    path('accounts/', include('allauth.socialaccount.urls')),
]+ static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

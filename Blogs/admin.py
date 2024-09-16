from django.contrib import admin

from .models import Post

class CustomPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, CustomPostAdmin)
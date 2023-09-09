from django.contrib import admin

from .models import Photo, Category

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ['title', 'category',]

admin.site.register(Category)
from django.urls import path

from .views import photo_list_view, photo_detail_view

urlpatterns = [
    path('', photo_list_view, name='photo_list'),
    path('photos/<int:pk>/', photo_detail_view, name='photo_detail'),
    path('add/', '', name='add_photo'),
]

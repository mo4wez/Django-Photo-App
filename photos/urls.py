from django.urls import path

from .views import photo_list_view, photo_detail_view, add_photo_view

urlpatterns = [
    path('', photo_list_view, name='photo_list'),
    path('<int:pk>/', photo_detail_view, name='photo_detail'),
    path('add/', add_photo_view, name='add_photo'),
]

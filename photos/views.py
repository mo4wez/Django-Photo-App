from django.shortcuts import render, get_object_or_404

from .models import Category, Photo


def photo_list_view(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {
        'categories': categories,
        'photos': photos,
    }

    return render(request, 'photos/photo_list.html', context)

def photo_detail_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    context = {
        'photo': photo
    }

    return render(request, 'photos/photo_detail.html', context)

def add_photo_view(request):
    categories = Category.objects.all()
    return render(request, 'photos/photo_create.html', context={'categories': categories,})
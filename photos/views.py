from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Category, Photo
from .forms import PhotoAddForm


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


@login_required
def add_photo_view(request):
    categories = Category.objects.all()
    photo_add_form = PhotoAddForm()

    if request.method == "POST":
        photo_add_form = PhotoAddForm(request.POST,)
        
        if photo_add_form.is_valid():
            photo_add_obj = photo_add_form.save(commit=False)
            photo_add_obj.user = request.user
            photo_add_obj.save()

    return render(request, 'photos/photo_create.html', context={'categories': categories, 'form':PhotoAddForm()})
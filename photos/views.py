from django.shortcuts import render, redirect, get_object_or_404
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

    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'None':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            title=data['title'],
            category=category,
            description=data['description'],
            image=image,

        )

        return redirect('photos:photo_list')

    return render(request, 'photos/photo_create.html', context={'categories': categories,})
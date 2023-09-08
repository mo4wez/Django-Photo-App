from django.shortcuts import render, HttpResponse


def photo_list_view(request):
    return render(request, 'photos/photo_list.html')

def photo_detail_view(request, pk):
    return render(request, 'photos/photo_detail.html')

def add_photo_view(request):
    return render(request, 'photos/photo_create.html')
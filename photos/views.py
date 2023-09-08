from django.shortcuts import render, HttpResponse


def photo_list_view(request):
    return HttpResponse('List')

def photo_detail_view(request, pk):
    return HttpResponse('Detail')

def add_photo_view(request):
    return HttpResponse('Add')
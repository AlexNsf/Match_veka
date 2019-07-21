from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def news(request):
    return render(request, 'pages/news.html')


def schedule(request):
    return render(request, 'pages/schedule.html')


def photo(request):
    return render(request, 'pages/photo.html')


def video(request):
    return render(request, 'pages/video.html')


def history(request):
    return render(request, 'pages/history.html')


def reg_form(request):
    return render(request, 'pages/reg_form.html')

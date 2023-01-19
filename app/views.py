from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.today()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = []
    for i, file in enumerate(listdir('.')):
        item = f'{str(i + 1)}. {file} <br>'
        files.append(item)
    return HttpResponse(files)

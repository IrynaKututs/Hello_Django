from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a=5+6
    return render(request, 'about.html',{'gretting':'hello', 'abc':a})# на странице, где путь views.about выведется все, что указано в файле
# about.html, который мы создали  в папке шаблоны
# каждому пути(функции представления) свой файл html

def home(request):
    return HttpResponse('This is my home')# на странице, где путь views.home выведется все, что
# написано в скобках
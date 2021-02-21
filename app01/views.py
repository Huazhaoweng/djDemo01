from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def mapmodel(request):
    return HttpResponse('地图应用首页！')


def calmodel(request):
    return HttpResponse('计算应用首页！')


def alamodel(request):
    return HttpResponse('告警应用首页！')

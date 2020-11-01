from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    return HttpResponse('hello')


def query1_view(request, year, month):
    return HttpResponse('hello_%s_%s' % (year, month))


def query2_view(request, year, month):
    return HttpResponse('hello2_%s_%s' % (year, month))


def query3_view(request, year, month, uname):
    return HttpResponse('hello3_%s_%s_%s' % (year, month, uname))

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    return HttpResponse('hello')


def query1_view(request, num):
    return HttpResponse('hello_%s' % num)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index_view(request):
    return render(request, 'index.html', {'n': 11})


def query1_view(request, year, month):
    return HttpResponse('hello_%s_%s' % (year, month))


def query2_view(request, year, month):
    return HttpResponse('hello2_%s_%s' % (year, month))


def query3_view(request, year, month, uname):
    return HttpResponse('hello3_%s_%s_%s' % (year, month, uname))


def query4_view(request, num):
    return HttpResponse('这是query4_view_%s' % num)


def index5_view(request):
    # 重定向（重新访问）
    return HttpResponseRedirect(reverse('q', args=(66,)))


def query6_view(request):
    return HttpResponse('query6_view')

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    scheme = request.scheme
    return HttpResponse('scheme:%s' % scheme)

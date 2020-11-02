from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    scheme = request.scheme
    path = request.path
    post1 = type(request.POST)
    return HttpResponse('scheme:%s' % post1)


def index1_view(request):
    return render(request, 'index2.html')

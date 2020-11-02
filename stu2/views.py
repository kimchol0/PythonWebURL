from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    scheme = request.scheme
    path = request.path
    return HttpResponse('scheme:%s' % path)


def index1_view(request):
    return render(request, 'index2.html')

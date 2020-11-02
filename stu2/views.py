from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    scheme = request.scheme
    body = request.body
    return HttpResponse('scheme:%s' % body)


def index1_view(request):
    return render(request, 'index2.html')

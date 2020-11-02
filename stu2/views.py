from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request):
    scheme = request.scheme
    path = request.path
    metainfo = request.META
    for m in metainfo:
        print(m)
    return HttpResponse('scheme:%s' % metainfo)


def index1_view(request):
    return render(request, 'index2.html')

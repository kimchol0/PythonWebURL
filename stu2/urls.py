from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index_view),
    re_path(r'query/$', views.index1_view)
]

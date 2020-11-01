from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index_view),
    re_path(r'^query/(\d{4})/(\d{2})', views.query1_view)
]

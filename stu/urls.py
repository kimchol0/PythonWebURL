from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index_view),
    re_path(r'^query1/(\d{4})/(\d{2})', views.query1_view),
    re_path(r'^query2/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.query2_view),
    # url(r'^register/', include('stu.urls')),
    re_path(r'^query3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.query3_view, {'uname': 'zhangsan'})
]

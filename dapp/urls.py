from django.conf.urls import url
from django.urls import path
from dapp import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name='index'),
    #path('desk', views.desk, name="desk"),
    path('submission', views.submission, name="submission"),
    url(r'^user/desk/$', views.desk),
    url(r'^user/create/$', views.create_user),
    url(r'^api/dapp$', csrf_exempt(views.dapp_list)),
    url(r'^api/dapp/(?P<pk>[0-9]+)$', csrf_exempt(views.dapp_detail))
    
]



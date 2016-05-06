from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^post/(?P<pk>\d+)/$', views.req_ing, name='req_ing'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^secrets/$', views.popular),
    url(r'^post$', views.post),
    url(r'^like/(?P<id>\d+)$', views.like, name = "like")
]
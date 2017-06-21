from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^remove$', views.remove)
]
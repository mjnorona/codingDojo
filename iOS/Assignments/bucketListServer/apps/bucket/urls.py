from django.conf.urls import include, url

from . import views  # This line is new!


urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^tasks$', views.tasks),
    url(r'^tasks/update$', views.update),
    url(r'^tasks/delete$', views.delete)
]
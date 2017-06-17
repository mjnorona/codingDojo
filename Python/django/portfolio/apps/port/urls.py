from django.conf.urls import url
from . import views  # This line is new!

urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^projects', views.projects),
    url(r'^about', views.about),
    url(r'^testimonials', views.test)
]
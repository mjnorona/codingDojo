from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.book_add),
    url(r'books/submit$', views.book_submit),
    url(r'books/(?P<id>\d+)$', views.book_reviews, name = "book_reviews"),
    url(r'users/(?P<id>\d+)$', views.user_reviews, name = "user_reviews"),
    url(r'/delete/(?P<id>\d+)$', views.review_delete, name = "review_delete"),
    url(r'logout$', views.logout)
]
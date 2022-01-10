from django.urls import path

from . import views

urlpatterns = [
    path('', views.comment_view, name='comment_view'),
    path('users', views.users, name='users'),
    path('clients', views.clients, name='clients'),
]
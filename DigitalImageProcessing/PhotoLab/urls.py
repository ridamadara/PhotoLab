from django.urls import path

from . import views

urlpatterns = [
    path('', views.comment_view, name='comment_view'),
    path('users', views.users, name='users'),
    path('clients', views.clients, name='clients'),

    path('resize', views.img_resize, name='resize'),
    path('blur', views.blur, name='blur'),
    path('filter', views.filter, name='filter'),
    path('brightness', views.brightness, name='brightness'),
    path('detect_edges', views.edge_detection, name='detect_edges'),
    path('grayscale', views.gray_scale, name='grayscale'),
    path('human_recognition', views.human_recognition, name='human_recognition'),
    path('text_recognition', views.text_recognition, name='text_recognition'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home')
]

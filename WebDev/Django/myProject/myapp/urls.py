from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),     # Main Site
    path('counter', views.counter, name='counter')
    ]
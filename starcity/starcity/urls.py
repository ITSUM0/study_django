from django.contrib import admin
from django.urls import path
from starcity import views

urlpatterns = [
    path('List/', views.index, name='index'),
]

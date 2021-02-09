from django.urls import path, include
from Famous import views

urlpatterns = [
    path('', views.index, name='index'),
]
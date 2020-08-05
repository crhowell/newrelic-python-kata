from django.urls import path

from . import views


urlpatterns = [
    path('kata4/', views.weather, name='weather'),
]

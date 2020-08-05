from django.urls import path

from . import views


urlpatterns = [
    path('kata1/', views.list, name='list'),
    path('kata2/', views.filtering, name='query'),
]

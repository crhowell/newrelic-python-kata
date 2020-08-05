from django.urls import path

from . import views


urlpatterns = [
    path('kata3/', views.factorial_h, name='factorial'),
]

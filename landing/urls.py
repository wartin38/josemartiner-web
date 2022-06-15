from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gracias/', views.gracias, name='gracias'),
]
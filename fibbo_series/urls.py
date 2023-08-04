from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_fibonacci, name='generate_fibonacci'),
]
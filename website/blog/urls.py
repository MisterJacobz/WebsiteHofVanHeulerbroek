from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('training_home', views.training_home, name='training_home'),
]

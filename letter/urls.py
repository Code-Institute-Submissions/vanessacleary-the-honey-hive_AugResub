from django.urls import path
from . import views

urlpatterns = [
    path('', views.letter, name='letter.urls'),
]
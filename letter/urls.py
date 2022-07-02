from django.urls import path
from . import views

urlpatterns = [
    path('', views.letter, name='letter'),
     path('mail_letter/', views.mail_letter, name='mail-letter')
]

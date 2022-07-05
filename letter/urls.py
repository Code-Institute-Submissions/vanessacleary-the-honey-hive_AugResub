from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_subscription, name='letter'),
    path('mail_letter/', views.mail_letter, name='mail-letter')
]

from django.urls import path
from OSCAPI import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('youtube/', views.obtener_datos_youtube, name='obtener_datos_youtube'),
]
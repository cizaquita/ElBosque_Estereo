from django.urls import path
 
from . import views

urlpatterns = [
	path('', views.conteo, name='conteo'),
	path('ind/', views.index, name='index'),
	path('audio/', views.audio, name='audio'),
	path('parrilla/', views.parrilla, name='parrilla'),
	path('get_parrilla/', views.get_parrilla, name='get_parrilla'),
	path('play/', views.play, name='play'),
]
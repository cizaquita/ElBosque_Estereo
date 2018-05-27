from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='conteo'),
	path('conteo/', views.conteo, name='conteo'),
	path('audio/', views.audio, name='audio'),
	path('parrilla/', views.parrilla, name='parrilla'),
]
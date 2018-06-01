from django.urls import path
 
from . import views

urlpatterns = [
	path('', views.conteo, name='conteo'),
	path('parrilla/', views.parrilla, name='parrilla'),
	path('get_parrilla/', views.get_parrilla, name='get_parrilla'),
	path('play/', views.play, name='play'),
]

handler404 = 'emisora.views.view_404' 
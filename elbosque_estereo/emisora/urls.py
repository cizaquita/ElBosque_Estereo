from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
 
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('audio/', views.audio, name='audio'),
	path('parrilla/', views.parrilla, name='parrilla'),
	path('get_parrilla/', views.get_parrilla, name='get_parrilla'),
	path('play/', views.play, name='play'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
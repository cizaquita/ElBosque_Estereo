from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index(request):
	return render(request, 'emisora/index.html')

def audio(request):
	return render(request, 'emisora/audio.html')

def parrilla(request):
	return render(request, 'emisora/parrilla/index.html')
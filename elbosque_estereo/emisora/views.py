from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index(request):
	return HttpResponse("Landing page under construction... <a href='/admin/'>Administración</a>")
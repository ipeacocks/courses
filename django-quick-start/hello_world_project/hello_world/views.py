from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return HttpResponse('<html><body>Hello, World!</body></html>')

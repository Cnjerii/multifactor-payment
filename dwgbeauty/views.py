from django.shortcuts import render
from django.http import HttpResponse

def payment(request):
	return HttpResponse('Payment Request')

def process(request):
		return HttpResponse('process Payment')

# Create your views here.

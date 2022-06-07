from django.shortcuts import render

def payment(request):
	return render(request, 'Payment_request/index.html')

def process(request):
		return render(request, 'Payment_request/process.html')

# Create your views here.

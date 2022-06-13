from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/dashboard.html')

def Products(request):
    return render(request, 'app/products.html')

def Customer(request):
    return render(request, 'app/Customer.html')
# Create your views here.

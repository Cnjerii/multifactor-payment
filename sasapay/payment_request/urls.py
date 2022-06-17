from django.urls import path, include
from . import views

urlpatterns = [
    path('request', views.payment),
    path('process', views.process)
]
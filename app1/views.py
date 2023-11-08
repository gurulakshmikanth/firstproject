from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Jampandu(request):
    return HttpResponse('hi i am jampandu how can i help u')

def Rani(request):
    return HttpResponse('i need 5k money')

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def portfolio(request):
    return render(request,"portfolio.html")

def resume(request):
    return render(request,'resume.html')

def port(request,portf):
    return HttpResponse(portf)
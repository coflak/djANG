from django.http import HttpResponse
from django.template import Template 
from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')
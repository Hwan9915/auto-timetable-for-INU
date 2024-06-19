from django.shortcuts import render
from django.http import request, HttpResponse
from django.template import loader

def make(request):
    a = "Hello, World!"
    template = loader.get_template('make/index.html')
    
    return render(request,"make/index.html", {'a':a})
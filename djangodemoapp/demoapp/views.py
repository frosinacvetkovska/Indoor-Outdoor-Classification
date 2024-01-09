
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def demoapp(request):
    template = loader.get_template('frontpage.html')
    return HttpResponse(template.render())
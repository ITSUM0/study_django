from django.shortcuts import render
from django.http import HttpResponse
from starcity.models import Employ

def index(request):
    employ=Employ.objects.all()
    print(employ[employname])
    return HttpResponse("Hello")
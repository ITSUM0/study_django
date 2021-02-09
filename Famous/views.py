from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("Hello")
    return render(request, 'Famous/index.html')

def restaurentDetail(request):
    return render(request, 'Famous/restaurentDetail.html')

def restaurentCreate(request):
    return render(request, 'Famous/restaurentCreate.html')

def categoryCreate(request):
    
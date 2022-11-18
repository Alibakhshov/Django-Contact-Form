from django.http import HttpResponse
from djang.shortcuts import render

def index(request):
    return render(request, 'index.html')
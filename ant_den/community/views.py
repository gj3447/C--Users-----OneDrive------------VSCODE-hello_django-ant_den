from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("하이염^^")
# Create your views here.

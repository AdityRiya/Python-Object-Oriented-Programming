from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(text):
    return HttpResponse("<em>The Text in embedded</em>")
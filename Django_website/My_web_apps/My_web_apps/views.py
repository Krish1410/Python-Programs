from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<H1>THere are multiple web apps in this project</H1><br><a href="/shop">Shoping App</a><br><a href="/blog">Bloging App</a>')
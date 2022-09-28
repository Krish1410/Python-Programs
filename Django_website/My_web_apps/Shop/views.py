from django.shortcuts import render
from django.http import HttpResponse
from . import models
from math import ceil

# Create your views here.

def index(request):
    # Products=models.product.objects.all()
    allprod=[]
    catprods=models.product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=models.product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprod.append([prod,range(1,nSlides),nSlides])
    params={'allprod':allprod}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contect(request):
    return HttpResponse('shop/contect.html')

def search(request):
    return HttpResponse('shop/search.html')

def product(request):
    return HttpResponse('shop/product.html')

def track(request):
    return HttpResponse('shop/track.html')



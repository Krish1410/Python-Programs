from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name='about'),
    path("contect",views.contect,name='Contect'),
    path("search",views.search,name='Search'),
    path("product",views.product,name='product'),
    path("track",views.track,name='Track'),
]
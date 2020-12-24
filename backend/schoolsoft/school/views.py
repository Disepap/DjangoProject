from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin

def index(request):
    print(dir(admin.site))
    return HttpResponse('<h1> hello </h1>')

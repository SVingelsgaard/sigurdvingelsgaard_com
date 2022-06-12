from django.shortcuts import render, redirect
from .models import *

#hompage
def home(request):
    return render(request, "home.html")

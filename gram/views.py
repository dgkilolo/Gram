from django.shortcuts import render, redirect
import datetime as datetime
from .models import Image

# Create your views here.
def home(request):
  
  return render(request, 'home.html')
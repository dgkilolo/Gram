from django.shortcuts import render, redirect
import datetime as datetime
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  images = Image.all_images()
  return render(request, 'home.html', {'images':images} )
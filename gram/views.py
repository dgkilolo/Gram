from django.shortcuts import render, redirect
import datetime as datetime

# Create your views here.
def home(request):
  return render(request, 'home.html')
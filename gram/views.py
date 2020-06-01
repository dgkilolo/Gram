from django.shortcuts import render, redirect
import datetime as datetime
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm

# Create your views here.

def home(request):
  images = Image.all_images()
  return render(request, 'home.html', {'images':images} )

@login_required(login_url='/accounts/login/')
def new_image(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewImageForm(request.POST, request.FILES)
    if form.is_valid():
      image = form.save(commit=False)
      image.save()
    return redirect('home')
  else:
    form = NewImageForm()
  return render(request, 'new_image.html', {"form":form} )
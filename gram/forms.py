from .models import Image
from django import forms

class NewImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['date']
    widgets = {
      
    }
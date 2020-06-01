from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
  picture = models.ImageField(upload_to='gram/')
  name = models.CharField(max_length=30, blank=True)
  caption = models.TextField(blank=True)
  date = models.DateTimeField(auto_now_add=True)

  def save_image(self):
    self.save()
  def delete_image(self):
    Image.objects.filter(pk=self.id).delete()
  
  @classmethod
  def all_images(cls):
    images = cls.objects.all()
    return images
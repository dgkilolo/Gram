from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
  picture = models.ImageField(upload_to='gram/')
  name = models.CharField(max_length=30, blank=True)
  caption = models.TextField(blank=True)
  date = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Image(models.Model):
  picture = models.ImageField(upload_to='gram/')
  name = models.CharField(max_length=30)
  caption = models.TextField()
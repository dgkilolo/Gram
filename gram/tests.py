from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
  # Set up method
  def setUp(self):
    self.image = Image(name="dog picture", caption="man's best friend")
  # Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))
  # Testing Save method
  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
  # Testing Delete method
  def test_delete_method(self):
    self.image.delete_image()
    images = Image.objects.all()
    self.assertTrue(len(images)<1)
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
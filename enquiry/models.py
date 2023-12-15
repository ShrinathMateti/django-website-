from django.db import models

class Enquiry(models.Model):
      name = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      number = models.TextField(max_length=100)
# Create your models here.

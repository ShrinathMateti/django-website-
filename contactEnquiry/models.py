from django.db import models

class contactEnquiry(models.Model):
      name = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      message = models.TextField(max_length=400)
# Create your models here.

from django.db import models

class Service(models.Model):
    service_icon= models.CharField(max_length=100)
    service_title= models.CharField(max_length=100)
    service_des= models.TextField(max_length=100)
# Create your models here.


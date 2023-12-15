from django.db import models
class Android(models.Model):
    android1_icon= models.CharField(max_length=300)
    android1_title= models.CharField(max_length=300)
    android1_des= models.TextField(max_length=300)
    android2_icon= models.CharField(max_length=300)
    android2_title= models.CharField(max_length=300)
    android2_des= models.TextField(max_length=300)
    android3_icon= models.CharField(max_length=300)
    android3_title= models.CharField(max_length=300)
    android3_des= models.TextField(max_length=300)
# Create your models here.

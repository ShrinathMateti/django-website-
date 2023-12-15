from django.db import models

class UIUX(models.Model):
    uiux1_icon= models.CharField(max_length=300)
    uiux1_title= models.CharField(max_length=300)
    uiux1_des= models.TextField(max_length=300)
    uiux2_icon= models.CharField(max_length=300)
    uiux2_title= models.CharField(max_length=300)
    uiux2_des= models.TextField(max_length=300)
    uiux3_icon= models.CharField(max_length=300)
    uiux3_title= models.CharField(max_length=300)
    uiux3_des= models.TextField(max_length=300)
# Create your models here.

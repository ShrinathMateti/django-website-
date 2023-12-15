from django.db import models

class About(models.Model):
    about_desc= models.CharField(max_length=300)
    about_team= models.TextField(max_length=300)
# Create your models here.

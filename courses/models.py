from django.db import models
from tinymce.models import HTMLField

class Courses(models.Model):
    course_title= models.CharField(max_length=100)
    course_desc= HTMLField()
# Create your models here.

from django.db import models

class Web(models.Model):
    web1_icon= models.CharField(max_length=300)
    web1_title= models.CharField(max_length=300)
    web1_des= models.TextField(max_length=300)
    web2_icon= models.CharField(max_length=300)
    web2_title= models.CharField(max_length=300)
    web2_des= models.TextField(max_length=300)
    web3_icon= models.CharField(max_length=300)
    web3_title= models.CharField(max_length=300)
    web3_des= models.TextField(max_length=300)
    web_image= models.FileField(upload_to="web/",max_length=255,null=True)
    
# Create your models here.

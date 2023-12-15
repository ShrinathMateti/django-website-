from django.contrib import admin
from web.models import Web
class ServiceAdmin(admin.ModelAdmin):
    list_display =('web1_icon','web1_title','web1_des','web2_icon','web2_title','web2_des','web3_icon','web3_title','web3_des')
    
admin.site.register(Web,ServiceAdmin)
# Register your models here.


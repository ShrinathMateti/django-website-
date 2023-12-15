from django.contrib import admin
from enquiry.models import Enquiry
class ServiceAdmin(admin.ModelAdmin):
    list_display =('name','email','number')
    
admin.site.register(Enquiry,ServiceAdmin)

# Register your models here.

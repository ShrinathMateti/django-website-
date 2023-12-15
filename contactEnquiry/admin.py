from django.contrib import admin
from contactEnquiry.models import contactEnquiry
class ServiceAdmin(admin.ModelAdmin):
    list_display =('name','email','message')
    
admin.site.register(contactEnquiry,ServiceAdmin)
# Register your models here.

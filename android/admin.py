from django.contrib import admin
from android.models import Android
class ServiceAdmin(admin.ModelAdmin):
    list_display =('android1_icon','android1_title','android1_des','android2_icon','android2_title','android2_des','android3_icon','android3_title','android3_des')
    
admin.site.register(Android,ServiceAdmin)
# Register your models here

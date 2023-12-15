from django.contrib import admin
from uiux.models import UIUX
class ServiceAdmin(admin.ModelAdmin):
    list_display =('uiux1_icon','uiux1_title','uiux1_des','uiux2_icon','uiux2_title','uiux2_des','uiux3_icon','uiux3_title','uiux3_des')
    
admin.site.register(UIUX,ServiceAdmin)
# Register your models here.

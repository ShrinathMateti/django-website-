from django.contrib import admin
from About.models import About
class ServiceAdmin(admin.ModelAdmin):
    list_display =('about_desc','about_team')
    
admin.site.register(About,ServiceAdmin)
# Register your models here.

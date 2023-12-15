from django.contrib import admin
from courses.models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_desc')
    
admin.site.register(Courses,CoursesAdmin)
# Register your models here.

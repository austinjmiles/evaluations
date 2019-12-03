from django.contrib import admin

# Register your models here.
from .models import Survey, Lab, Student

admin.site.register(Survey)
admin.site.register(Lab)
admin.site.register(Student)

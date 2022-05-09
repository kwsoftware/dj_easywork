from django.contrib import admin
from easy_app import models

# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.DepartmentType)
admin.site.register(models.Machine)
admin.site.register(models.User)
admin.site.register(models.Operation)
admin.site.register(models.Shift)
admin.site.register(models.Admin)
admin.site.register(models.Supervisor)
admin.site.register(models.Expert)
admin.site.register(models.Operator)

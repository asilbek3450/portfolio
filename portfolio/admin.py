from django.contrib import admin

from .models import Contact, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Contact)

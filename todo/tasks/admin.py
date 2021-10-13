from django.contrib import admin

# Register your models here.
from .models import Task

#importando o model Task para o admin
admin.site.register(Task)
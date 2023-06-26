from django.contrib import admin
from .models import Calorie

# Register your models here.
class Calorieadmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Calorie,Calorieadmin)

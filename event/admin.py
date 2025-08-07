from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Event)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name','date','contact_name')
    search_fields = ['name']
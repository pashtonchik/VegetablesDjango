from django.contrib import admin
from .models import *


@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
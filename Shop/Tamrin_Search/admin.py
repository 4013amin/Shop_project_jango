from django.contrib import admin

from .models import Data


# Register your models here.
@admin.register(Data)
class Admin_Data(admin.ModelAdmin):
    list_display = ('username', 'title')

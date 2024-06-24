from django.contrib import admin

from .models import Users

# Register your models here.
admin.site.register(Users)


class Admin_Users(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')

from django.contrib import admin
from .models import DataBase
# Register your models here.

class DbAdmin(admin.ModelAdmin):
    fields = ['host', 'port', 'username', 'password','db','title']


admin.site.register(DataBase,DbAdmin)
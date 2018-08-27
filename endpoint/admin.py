from django.contrib import admin
from .models import EndPoint,BaseUrl
# Register your models here.

class EndPointAdmin(admin.ModelAdmin):
    # fields = ['endpoint','host','description']
    pass
    

admin.site.register(EndPoint, EndPointAdmin)
admin.site.register(BaseUrl)


from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('passward','user_name')
    
admin.site.register(Service,ServiceAdmin)
# Register your models here.

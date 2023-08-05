from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    pass

class ClinicAdmin(admin.ModelAdmin):
    pass


admin.site.register(User,UserAdmin)
admin.site.register(Clinic,ClinicAdmin)
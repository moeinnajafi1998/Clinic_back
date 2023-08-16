from django.contrib import admin
from .models import *


class RequestSessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(RequestSession,RequestSessionAdmin)
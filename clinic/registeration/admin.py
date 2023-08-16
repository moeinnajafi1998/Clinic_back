from django.contrib import admin
from .models import *


class RequestSessionAdmin(admin.ModelAdmin):
    pass

class MedicalAppointmentAdmin(admin.ModelAdmin):
    pass


class RequestGoodsAdmin(admin.ModelAdmin):
    pass

admin.site.register(RequestSession,RequestSessionAdmin)
admin.site.register(MedicalAppointment,MedicalAppointmentAdmin)
admin.site.register(RequestGoods,RequestGoodsAdmin)

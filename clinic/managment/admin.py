from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    pass

class ClinicAdmin(admin.ModelAdmin):
    pass

class WhareHouseAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass



admin.site.register(User,UserAdmin)
admin.site.register(Clinic,ClinicAdmin)
admin.site.register(WhareHouse,WhareHouseAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)



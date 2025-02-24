from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustuserAdmin(UserAdmin):
   list_display=('username','email','role','is_staff','is_superuser')


admin.site.register(Custuser,CustuserAdmin)
admin.site.register(Packages)
admin.site.register(Booking)




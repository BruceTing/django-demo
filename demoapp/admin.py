from django.contrib import admin

from .models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Users, UsersAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class FotoRumahInline(admin.TabularInline):
    model = FotoRumah
    extra = 1

class RumahAdmin(admin.ModelAdmin):
    inlines = (FotoRumahInline,)


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    
admin.site.register(Rumah, RumahAdmin)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

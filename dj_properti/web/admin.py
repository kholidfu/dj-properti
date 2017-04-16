from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms

from .models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class FotoRumahInline(admin.TabularInline):
    model = FotoRumah
    extra = 6


class RumahAdmin(admin.ModelAdmin):
    inlines = (FotoRumahInline,)
    prepopulated_fields = {'judul_iklan_slug': ('judul_iklan',)}
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
    exclude = ('user',)


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class FasilitasAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nama_fasilitas_slug': ('nama_fasilitas',)}


admin.site.register(Fasilitas, FasilitasAdmin)
admin.site.register(Rumah, RumahAdmin)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

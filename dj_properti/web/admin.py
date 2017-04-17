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
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
    exclude = ('judul_iklan_slug', 'user',)

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.

        Example of request all listings by current user:

        >>> Rumah.objects.filter(user__username='admin')

        """
        if not change:
            obj.user = request.user
        obj.save()


class FotoTanahInline(admin.TabularInline):
    model = FotoTanah
    extra = 6


class TanahAdmin(admin.ModelAdmin):
    inlines = (FotoTanahInline,)
    exclude = ('judul_iklan_slug', 'user',)

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.

        Example of request all listings by current user:

        >>> Rumah.objects.filter(user__username='admin')

        """
        if not change:
            obj.user = request.user
        obj.save()


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class FasilitasAdmin(admin.ModelAdmin):
    exclude = ('nama_fasilitas_slug',)


admin.site.register(Fasilitas, FasilitasAdmin)
admin.site.register(Rumah, RumahAdmin)
admin.site.register(Tanah, TanahAdmin)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

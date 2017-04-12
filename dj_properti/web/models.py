from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .choices import *


class Profile(models.Model):
    """Extended User Profile."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    provinsi = models.PositiveSmallIntegerField(
        choices=PROVINSI,
        blank=True, null=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    email_able = models.BooleanField(
        default=False,
        verbose_name='Saya tidak ingin dihubungi lewat email'
    )
    no_telepon = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    wa_available = models.BooleanField(
        default=False,
        verbose_name='Saya bisa dihubungi lewat WhatsApp'
    )
    pinbb = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Pin BB'
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.profile.save()

class Category(models.Model):
    """Category Models."""
    pass


class House(models.Model):
    """House models."""

    title = models.CharField(
        max_length=255
    )
    price = models.IntegerField()
    lotsize = models.IntegerField(
        verbose_name='Luas Tanah'
    )  # luas tanah
    housesize = models.IntegerField()  # luas rumah
    floortype = models.CharField(
        max_length=255
    )  # jenis lantai
    bedroom = models.PositiveSmallIntegerField(
        choices=ROOM_NUMBER
    )
    bathroom = models.PositiveSmallIntegerField(
        choices=ROOM_NUMBER
    )
    certificate_status = models.CharField(
        choices=CERTIFICATE_STATUS,
        max_length=255
    )
    facilities = models.CharField(
        choices=FACILITIES,
        max_length=255
    )
    address = models.TextField()
    description = models.TextField(
        max_length=255
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class HouseImage(models.Model):
    house_image = models.ForeignKey(House)
    image = models.ImageField(
        upload_to='assets/',
        blank=True,
        null=True,
        max_length=1000,  # max_length of filename
    )


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.template.defaultfilters import slugify

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


class Fasilitas(models.Model):
    """Fasilitas Model."""
    nama_fasilitas = models.CharField(
        max_length=255,
        help_text=_('Pilih fasilitas yang tersedia di rumah')
    )
    nama_fasilitas_slug = models.SlugField()


    class Meta:
        verbose_name_plural = 'Fasilitas'


    def save(self, *args, **kwargs):
        # override save for slug field
        self.nama_fasilitas_slug = slugify(self.nama_fasilitas)
        super(Fasilitas, self).save(*args, **kwargs)

    def __str__(self):
        return self.nama_fasilitas


class Rumah(models.Model):
    """Rumah models."""

    judul_iklan = models.CharField(
        max_length=255,
        help_text=_('Masukkan judul iklan')
    )
    judul_iklan_slug = models.SlugField(
        help_text=_('Otomatis terisi, biarkan saja')
    )
    status_iklan = models.PositiveSmallIntegerField(
        choices=TIPE_LISTING,
        verbose_name=('Status Iklan'),
        help_text=('Pilih jenis iklan'),
    )
    harga = models.IntegerField(
        help_text=_('Masukkan harga rumah')
    )
    luas_tanah = models.IntegerField(
        verbose_name='Luas Tanah',
        help_text=_('Satuan meter persegi')
    )
    luas_rumah = models.IntegerField(
        verbose_name='Luas Rumah',
        help_text=_('Satuan meter persegi')
    )
    jenis_lantai = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Jenis Lantai',
        help_text=_('Jenis lantai')
    )
    jumlah_kamar_tidur = models.PositiveSmallIntegerField(
        choices=JUMLAH_KAMAR,
        help_text=_('Pilih jumlah kamar tidur')
    )
    jumlah_kamar_mandi = models.PositiveSmallIntegerField(
        choices=JUMLAH_KAMAR,
        help_text=_('Pilih jumlah kamar mandi')
    )
    status_sertifikat = models.PositiveSmallIntegerField(
        choices=STATUS_SERTIFIKAT,
        help_text=_('Pilih jenis sertifikat')
    )
    fasilitas = models.ManyToManyField(
        Fasilitas,
        blank=True,
    )
    alamat = models.TextField(
        help_text=_('Masukkan alamat detail')
    )
    deskripsi_iklan = models.TextField(
        help_text=_('Masukkan deskripsi iklan')
    )
    # auto fill in save
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('Pilih user')
    )


    class Meta:
        verbose_name_plural = 'Rumah'


    def save(self, *args, **kwargs):
        # override save for slug field
        self.judul_iklan_slug = slugify(self.judul_iklan)
        super(Rumah, self).save(*args, **kwargs)

    def __str__(self):
        return self.judul_iklan


class FotoRumah(models.Model):
    foto_rumah = models.ForeignKey(Rumah)
    foto = models.ImageField(
        upload_to='assets/rumah/',
        blank=True,
        null=True,
        max_length=1000,  # max_length of filename
    )


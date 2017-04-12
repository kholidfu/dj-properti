from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Extended User Profile."""
    ACEH = 1
    BALI = 2
    BANGKA_BELITUNG = 3
    BANTEN = 4
    BENGKULU = 5
    GORONTALO = 6
    DKI = 7
    JAMBI = 8
    JABAR = 9
    JATENG = 10
    JATIM = 11
    KALBAR = 12
    KALSEL = 13
    KALTENG = 14
    KALTIM = 15
    KALUT = 16
    KEPRI = 17
    LAMPUNG = 18
    MALUKU = 19
    MALUT = 20
    NTB = 21
    NTT = 22
    PAPUA = 23
    PAPUA_BARAT = 24
    RIAU = 25
    SULBAR = 26
    SULSEL = 27
    SULTENG = 28
    SULTENGGA = 29
    SULUT = 30
    SUMBAR = 31
    SUMSEL = 32
    SUMUT = 33
    DIY = 34
    PROVINSI = (
        (ACEH, 'Daerah Istimewa Aceh'),
        (BALI, 'Bali'),
        (BANGKA_BELITUNG, 'Bangka Belitung'),
        (BANTEN, 'Banten'),
        (BENGKULU, 'Bengkulu'),
        (GORONTALO, 'Gorontalo'),
        (DKI, 'Daerah Khusus Ibukota Jakarta'),
        (JAMBI, 'Jambi'),
        (JABAR, 'Jawa Barat'),
        (JATENG, 'Jawa Tengah'),
        (JATIM, 'Jawa Timur'),
        (KALBAR, 'Kalimantan Barat'),
        (KALSEL, 'Kalimantan Selatan'),
        (KALTENG, 'Kalimantan Tengah'),
        (KALTIM, 'Kalimantan Timur'),
        (KALUT, 'Kalimantan Utara'),
        (KEPRI, 'Kepulauan Riau'),
        (LAMPUNG, 'Lampung'),
        (MALUKU, 'Maluku'),
        (MALUT, 'Maluku Utara'),
        (NTB, 'Nusa Tenggara Barat'),
        (NTT, 'Nusa Tenggara Timur'),
        (PAPUA, 'Papua'),
        (PAPUA_BARAT, 'Papua Barat'),
        (RIAU, 'Riau'),
        (SULBAR, 'Sulawesi Barat'),
        (SULSEL, 'Sulawesi Selatan'),
        (SULTENG, 'Sulawesi Tengah'),
        (SULTENGGA, 'Sulawesi Tenggara'),
        (SULUT, 'Sulawesi Utara'),
        (SUMBAR, 'Sumatera Barat'),
        (SUMSEL, 'Sumatera Selatan'),
        (SUMUT, 'Sumatera Utara'),
        (DIY, 'Daerah Istimewa Yogyakarta'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provinsi = models.PositiveSmallIntegerField(choices=PROVINSI,
                                                blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email_able = models.BooleanField(default=False,
                                     verbose_name='Saya tidak ingin dihubungi lewat email')
    no_telepon = models.CharField(max_length=255, blank=True, null=True)
    wa_available = models.BooleanField(default=False,
                                       verbose_name='Saya bisa dihubungi lewat WhatsApp')
    pinbb = models.CharField(max_length=255, blank=True, null=True, verbose_name='Pin BB')

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

    # LISTING TYPE
    JUAL = 1
    BELI = 2
    SEWA = 3
    LISTING_TYPE = (
        (JUAL, 'Jual'),
        (BELI, 'Beli'),
        (SEWA, 'Sewa'),
    )

    # ROOM_NUMBER
    SATU = 1
    DUA = 2
    TIGA = 3
    EMPAT = 4
    LIMA = 5
    ENAM = 6
    ROOM_NUMBER = (
        (SATU, 1),
        (DUA, 2),
        (TIGA, 3),
        (EMPAT, 4),
        (LIMA, 5),
        (ENAM, 6),
    )

    # CERTIFICATE_STATUS
    SHM = 1
    HGB = 2
    LAINNYA = 3
    CERTIFICATE_STATUS = (
        (SHM, 'SHM - Sertifikat Hak Milik'),
        (HGB, 'HGB - Hak Guna Bangunan'),
        (LAINNYA, 'Lainnya - PPJB, Girik, Adat, dll'),
    )
    
    # FACILITIES
    AC = 1
    SWIMMING_POOL = 2
    CARPORT = 3
    GARDEN = 4
    GARASI = 5
    TELEPHONE = 6
    PAM = 7
    WATER_HEATER = 8
    REFRIGERATOR = 9
    STOVE = 10
    MICROWAVE = 11
    OVEN = 12
    FIRE_EXTENGUISHER = 13
    GORDYN = 14
    FACILITIES = (
        (AC, 'AC'),
        (SWIMMING_POOL, 'Swimming Pool'),
        (CARPORT, 'Carport'),
        (GARDEN, 'Garden'),
        (GARASI, 'Garasi'),
        (TELEPHONE, 'Telephone'),
        (PAM, 'PAM'),
        (WATER_HEATER, 'Water Heater'),
        (REFRIGERATOR, 'Refrigerator'),
        (STOVE, 'Stove'),
        (MICROWAVE, 'Microwave'),
        (OVEN, 'Oven'),
        (FIRE_EXTENGUISHER, 'Fire Extenguisher'),
        (GORDYN, 'Gordyn'),
    )

    title = models.CharField(max_length=255)
    # category = models.ForeignKey(Category)
    price = models.IntegerField()
    lotsize = models.IntegerField(verbose_name='Luas Tanah')  # luas tanah
    housesize = models.IntegerField()  # luas rumah
    floortype = models.CharField(max_length=255)  # jenis lantai
    bedroom = models.PositiveSmallIntegerField(choices=ROOM_NUMBER)
    bathroom = models.PositiveSmallIntegerField(choices=ROOM_NUMBER)
    certificate_status = models.CharField(choices=CERTIFICATE_STATUS,
                                          max_length=255)
    facilities = models.CharField(choices=FACILITIES, max_length=255)
    address = models.TextField()
    description = models.TextField(max_length=255)
    # images = onetomany
    user = models.ForeignKey(User, on_delete=models.CASCADE)



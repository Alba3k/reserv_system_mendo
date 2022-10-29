from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from PIL import Image


class Type(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='тип номера', default='None')
    slug = models.SlugField(('Slug'), max_length=50, db_index=True, validators=[], blank=True)
    short_desc = models.CharField(max_length=30, null=True, blank=True, verbose_name='тип номера', default='None')

    class Meta:
        verbose_name_plural = 'типы номеров'
        verbose_name = 'тип номера'
        ordering = ['name']

    @staticmethod
    def get_all_types():
        return Type.objects.all()

    def __str__(self):
        return (self.name).upper()


class Room(models.Model):
    number = models.CharField(max_length=20, null=True, blank=True, verbose_name='номер')
    slug = models.SlugField(('Slug'), max_length=50, db_index=True, validators=[], blank=True)
    room_type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE, verbose_name='цена и тип номера')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name='цена за номер в USD')
    
    room_image = models.ImageField(upload_to='rooms_pics')
    room_image_2 = models.ImageField(blank=True, null=True, upload_to='rooms_pics')
    room_image_3 = models.ImageField(blank=True, null=True, upload_to='rooms_pics')
    room_image_4 = models.ImageField(blank=True, null=True, upload_to='rooms_pics')
    capacity = models.IntegerField(verbose_name='количество гостей')

    number_of_beds = models.IntegerField(verbose_name='количество кроватей')
    description = models.TextField(verbose_name='краткое описание')

    tv_choices = (('NONE','Нет'),('FLAT TV', 'Flat TV'),('FLAT LED TV', 'Flat Led TV'),)
    room_tv = models.CharField(max_length=20, choices=tv_choices, default='NONE', verbose_name='наличие тв')

    wifi_choices = (('NOT AVAILABLE', 'Нет'),('AVAILABLE', 'Есть'),)
    room_wifi = models.CharField(max_length=20, choices=wifi_choices, default='NOT AVAILABLE', verbose_name='наличие wi-fi')

    cond_choices = (('NOT AVAILABLE', 'Нет'),('AVAILABLE', 'Есть'),)
    room_cond = models.CharField(max_length=30, choices=cond_choices, default='NOT AVAILABLE', verbose_name='наличие кондиционера')

    bathroom_choices = (('ATTACHED','Есть'),('NOT ATTACHED','Нет'),)
    room_bathroom = models.CharField(max_length=30, choices=bathroom_choices, default='ATTACHED', verbose_name='наличие ванной, душевой')

    status_reservation = models.BooleanField(default=False)

    rating_stars = models.IntegerField(blank=True, null=True, default=0, verbose_name='рейтинг')
    best_choice = models.BooleanField(default=False, verbose_name='рекомендация администрации')
   
    class Meta:
        verbose_name_plural = 'номера'
        verbose_name = 'номер'
        ordering = ['number']

    @staticmethod
    def get_room_by_id(ids):
        return Room.objects.filter(id_in=ids)

    @staticmethod
    def get_all_rooms():
        return Room.objects.all()

    @staticmethod
    def get_all_room_by_type_id(type_id):
        if type_id:
            return Room.objects.filter(type=type_id)
        else:
            return Room.get_all_products();
   
    def __str__(self):
        return str(self.number) + '. ' + str(self.room_type)

    def save(self):
        super().save()
        img = Image.open(self.room_image.path)
        if img.height!=768 or img.width!=1366:
            output_size = (1366,768)
            img.thumbnail(output_size)
            img.save(self.room_image.path)

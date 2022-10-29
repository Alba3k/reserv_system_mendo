from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

from rooms.models import Room


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name='номер')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='гость')

    reservation_date = models.DateTimeField(default=timezone.now, verbose_name='дата и время бронирование')
    from_date = models.DateField(null=True, verbose_name='с')
    to_date = models.DateField(null=True, verbose_name='по')
    
    number_of_guests = models.IntegerField(blank=True, null=True, default=1, verbose_name='количество гостей')

    total_days = models.IntegerField(blank=True, null=True, verbose_name='всего дней')
    total_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name='итоговая сумма')

    time_slot = models.CharField(max_length=10000, blank=True, null=True, verbose_name='перечень занятых дней')
    notes = models.TextField(blank=True, null=True, verbose_name='примечание')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        td = self.to_date - self.from_date
        self.total_days = int(td.total_seconds() / 86400)
        self.total_price = self.room.price * self.total_days

        d1 = self.from_date
        d2 = self.to_date
        days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
        res = [day.strftime('%Y-%m-%d') for day in days]

        self.time_slot = res
        super().save(force_insert, force_update, using, update_fields)

    @staticmethod
    def get_booking_by_customer(customer_id):
        return Booking.objects.filter(customer=customer_id).order_by('-reservation_date')

    def __str__(self):
        return f'{self.customer, self.room.number}'

    class Meta:
        verbose_name_plural = 'бронирование номеров'
        verbose_name = 'бронирование номеров'
        ordering = ['-reservation_date']
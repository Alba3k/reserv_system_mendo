from django.contrib import admin
from . models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'customer', 'number_of_guests', 'reservation_date', 'from_date', 'to_date', 'total_days', 'total_price',)
    list_display_links = ('room',)
    list_filter = ('room', 'reservation_date', 'number_of_guests', 'total_days',)
    search_fields = ('room__startswith',)
    raw_id_fields = ('room',)
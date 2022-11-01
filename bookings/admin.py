from django.contrib import admin
from . models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'room', 'number_of_guests', 'reservation_date', 'from_date', 'to_date', 'total_days', 'total_price', 'booking_status',)
    list_display_links = ('package_id', 'room',)
    list_filter = ('room', 'reservation_date', 'number_of_guests', 'total_days', 'booking_status',)
    search_fields = ('room__startswith',)
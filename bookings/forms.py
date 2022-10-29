from django.contrib.auth.models import User
from django import forms

from . models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('room', 'from_date', 'to_date', 'number_of_guests', 'notes',)
from django.views.generic import ListView, TemplateView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils import timezone
from django.db import connection

from datetime import datetime, date, time, timedelta
import sqlite3

from rooms.models import Room, Type
from rooms.views import book_func

from . forms import BookingForm
from . models import Booking


def time_slot_func(date_first, date_last):
    d1 = datetime.strptime(date_first, '%Y-%m-%d')
    d2 = datetime.strptime(date_last, '%Y-%m-%d')

    days = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]

    res = [day.strftime('%Y-%m-%d') for day in days]
    del res[0]
    res.pop()
    day_for_booking = set(res)
    # получаем временной слот для бронирования в виде сета
    return day_for_booking


def get_booking_id(room):
    lst = []
    result = Booking.objects.values('time_slot').filter(room_id = room)
    for row in result:
        row = row['time_slot']
        row = row.replace('*', '')
        row = row.replace(')', '')
        row = row.replace('(', '')
        row = row.replace('"', '')
        row = row.replace('*', '')
        row = row.replace('»', '')
        row = row.replace('«', '')
        row = row.replace(',', '')
        row = row.replace('.', '')
        row = row.replace("'", "")
        row = row.lstrip('[')
        row = row.rstrip(']')
        row = row.split()
        row = set(row)
        lst.append(row)
    # сет брони по выбранному номеру
    return lst


def final_check(lst, res_time):
    free_room_num = []
    for row in lst:
        if res_time.isdisjoint(row) == True:
            free_room_num.append('open')
        else:
            free_room_num.append('close')
    if free_room_num.count('close') > 0:
        res = False
    else:
        res = True
    return res


def check_capacity(number_of_guests, room):
    res = Room.objects.values('capacity').filter(pk = room)
    for value in res:
        cap_num = value['capacity']
    cap_num = int(cap_num)
    if int(number_of_guests) <= cap_num:
        res = True
    else:
        res = False
    return res


@login_required
def reserved(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                room = request.POST.get('room')

                from_date = request.POST.get('from_date')
                to_date = request.POST.get('to_date')
        
                number_of_guests = request.POST.get('number_of_guests')

                res_time = time_slot_func(from_date, to_date)
                res_num = get_booking_id(room)
                res = final_check(res_num, res_time)
                capacity_res = check_capacity(number_of_guests, room)

                if (res and capacity_res) == True:
                    itogo = True
                else:
                    itogo = False

                if itogo:
                    post = form.save(commit=False)
                    post.customer = User.objects.get(username=request.user)
                    post.save()

                    messages.success(request, f'Бронирование номера на период с {from_date} по {to_date}, для {number_of_guests} гостей создано.')
                    return redirect('index')
                else:
                    form = BookingForm()
            except IndexError:
                form = BookingForm()
    else:
        form = BookingForm()
    return render(request, 'web/reserved.html', {'form': form})
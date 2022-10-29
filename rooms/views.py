from django.views.generic import ListView, TemplateView, DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime, date, time, timedelta

from bookings.models import Booking
from . models import Room, Type


class HomePage(ListView):
    queryset = Type.objects.order_by('name')
    template_name = 'web/home.html'
    context_object_name = 'type_room'

    def get_context_data(self, **kwargs):
        room = Room.objects.all()
        context = super().get_context_data(**kwargs)
        context['features_room'] = room[0:5]
        context['total_room'] = room.count()
        return context


class CatalogPage(ListView):
    queryset = Room.objects.order_by('number')
    paginate_by=9
    template_name = 'web/catalog.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        room = Room.objects.all()
        context = super().get_context_data(**kwargs)
        context['total_room'] = room.count()
        return context


def show_room(request, room_slug):
    room_detail = Room.objects.get(slug=room_slug)
    cat_type = Type.objects.all()
    context = {
        'room':room_detail,
        'cat':cat_type
            }
    return render(request, 'web/room.html', context)
    

def time_slot_func(date_first, date_last):
    d1 = datetime.strptime(date_first, '%m/%d/%Y')
    d2 = datetime.strptime(date_last, '%m/%d/%Y')
    days = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]

    res = [day.strftime('%Y-%m-%d') for day in days]
    del res[0]
    res.pop()
    day_for_booking = set(res)
    return day_for_booking


def book_func(res_num):
    free_room = []
    for i in res_num:
        free_room_num = []
      
        sample_date = i[0]
        free_room_num.append((i[0], i[1]))

        result = Booking.objects.values('time_slot').filter(room_id = sample_date)
      
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
            if res_time.isdisjoint(row) == True:
                free_room_num.append('open')
            else:
                free_room_num.append('close')
        if free_room_num.count('close') > 0:
            continue
        else:
            free_room.append(i[1])
    return free_room


def search(request):
    if request.method == 'POST':
        try:
            category = request.POST.get("room_type", None)
            date_first = request.POST.get("fromDate", "10.10.2022")
            date_last = request.POST.get("toDate", "12.10.2022")
            num_guest = request.POST.get("adults", 1)
            num_child = request.POST.get("children", 0)

            global res_time
            res_time = time_slot_func(date_first, date_last)

            temp = Type.objects.get(name=category)
            cat_id = temp.id
            temp = Room.objects.filter(room_type_id = cat_id)
            res_num = [(i.id, i.number) for i in temp]

            res_room = book_func(res_num)
            total = len(res_room) 

            context = {
                'category':category,
                'date_first':date_first,
                'date_last':date_last,
                'num_guest':num_guest,
                'num_child':num_child,

                'total':total,
                'res_room':res_room,
                }

            return render(request, 'web/search_rooms.html', context)

        except IndexError:
            return render(request, 'error/404.html')

        except temp.DoesNotExist:
            return render(request, 'error/404.html')

        except UnboundLocalError:
            return render(request, 'error/404.html')
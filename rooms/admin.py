from django.contrib import admin
from . models import Type, Room


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ('name', 'short_desc',)
	list_display_links = ('name',)
	list_filter = ('short_desc',)
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	list_display = ('number', 'price', 'room_type', 'capacity', 'number_of_beds')
	list_display_links = ('number',)
	list_filter = ('room_type', 'price', 'capacity', 'number_of_beds')
	search_fields = ('number__startswith',)
	prepopulated_fields = {'slug': ('number',)}
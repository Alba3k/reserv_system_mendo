from django.contrib import admin
from . models import Post, Cat


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'slug', 'created', 'publish', 'status',)
    list_display_links = ('title', 'slug',)
    list_filter = ('cat', 'status',)
    search_fields = ('title__startswith',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Cat)
class postAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    list_display_links = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
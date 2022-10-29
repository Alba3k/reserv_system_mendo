from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')
    slug = models.SlugField(('Slug'), max_length=50, db_index=True, validators=[], blank=True)

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'черновик'),
        ('published', 'опубликовано'),
    )
    title = models.CharField(max_length=255, verbose_name='заголовок')
    cat = models.ForeignKey(Cat, on_delete=models.PROTECT, verbose_name='категория новостей', null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    mini_content = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='мини заголовок')
    body = models.TextField(blank=True, verbose_name='текст новости')
    photo_1 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_2 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_3 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_4 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_5 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_6 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_7 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)
    photo_8 = models.ImageField(
        upload_to='news_pics/%Y/%m/%d/', null=True, blank=True,)

    publish = models.DateTimeField(default=timezone.now, verbose_name='время публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='время изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='статус публикации')

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])

    def __str__(self):
        return self.title
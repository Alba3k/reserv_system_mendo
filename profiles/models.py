from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     class Meta:
#         verbose_name_plural = 'профили пользователей'
#         verbose_name = 'профиль пользователя'
#         ordering = ['user']

#     def __str__(self):
#         return self.user.username
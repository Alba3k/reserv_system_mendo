# from django.core.exceptions import ObjectDoesNotExist
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile


# @receiver(post_save, sender=User)
# def save_or_create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         try:
#             instance.profile.save()
#         except ObjectDoesNotExist:
#             Profile.objects.create(user=instance)
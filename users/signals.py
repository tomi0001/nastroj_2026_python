from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User2 = get_user_model()

@receiver(post_save, sender=User2)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
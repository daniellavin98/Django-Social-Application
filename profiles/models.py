from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField


# Create ynew profile model 

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="profile"

    )

    image = ImageField(upload_to='profiles')

    def __str__(self):
        return self.user.username



# signal - when user is created, create new profile
@receiver(post_save, sender=User)
def create_users_profile(sender, instance, created, **kwrags):

    if created:
        Profile.objects.create(user=instance)

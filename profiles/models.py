from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
This needed to get around a bug
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            profile = Profile.objects.create(owner=instance)
            print("Profile created:", profile)
        except Exception as e:
            print("Error creating profile:", e)

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default/default_profile_vbamal'
    )

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.owner}'s profile"

# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(owner=instance)

# post_save.connect(create_profile, sender=User)
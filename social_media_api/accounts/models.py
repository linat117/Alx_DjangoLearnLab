from django.db import models
from django.contrib.auth.models import AbstractUser 

def profile_upload_path(instance, filename):
    return f"Profile_pictures/user_{instance.id}/{filename}" 

class User(AbstractUser):
    bio = models.TextField(blank= True)
    profile_picture = models.ImageField(upload_to = profile_upload_path, blank= True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",  # reverse side: who follows me
        blank=True,
    )
    def __str__(self):
        return self.username

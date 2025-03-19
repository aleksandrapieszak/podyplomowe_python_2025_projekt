from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    friends = models.ForeignKey('self', on_delete=models.CASCADE, related_name='user_friends', blank=True, null=True)

    def __str__(self):
        return self.username

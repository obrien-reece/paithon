from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    shortintro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profileimages", default="profileimages/default.png",
        blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

"""The base doctor model"""
import os

from django.db import models


class Doctor(models.Model):
    """Doctor model"""
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to="media/", blank=True)
    specialisation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.fullname)

    def get_absolute_image(self):
        """returns the absolute path for the profile pic"""
        return os.path.join('/doctor/media', self.profilepic.name)

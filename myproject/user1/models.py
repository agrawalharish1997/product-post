# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
class post(models.Model):
    text=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(blank=True)
    updated = models.DateField(blank=True)
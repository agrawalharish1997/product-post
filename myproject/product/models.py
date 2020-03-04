# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=100)
    weight=models.IntegerField()
    price=models.IntegerField()
    created_at= models.DateField()
    updated_at= models.DateField()

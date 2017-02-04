# -*- coding: utf-8 -*-

# django models
from django.db import models
#User genişletme
from django.contrib.auth.models import AbstractUser

# yeni user model
class User(AbstractUser):
    avatar = models.CharField(max_length=100,help_text="Profil")
    bio = models.TextField(blank=False,help_text="Biyografi")
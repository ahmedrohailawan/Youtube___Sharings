import email
from email import message
from email.policy import default
from pickle import TRUE
from pyexpat import model
from django.db.models.base import Model
from django.forms import IntegerField

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

class User(AbstractUser):
    name = models.CharField(max_length=122,null=True,default="Web Knowledge")
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True,default="Write about yourself")
    avatar = models.ImageField(null=True,default="avatar.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=False)
    mobile = models.BigIntegerField(unique=True, blank=True, null=True)
    is_staff=models.BooleanField(default=False)
    objects = UserManager()
    REQUIRED_FIELDS = ['password','username']
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name='user'

class Address(models.Model):
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Relation(models.Model):
    relation_type = models.CharField(max_length=100, blank=False)
    status = models.CharField(unique=False, max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_relation')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_relation')

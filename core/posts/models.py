from django.db import models
from core.users.models import Address
from core.users.models import User

class Posts(models.Model):
    text = models.CharField(max_length=100, blank=False)
    image =models.ImageField(default='default.png',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='UserPosts')
    address = models.ForeignKey(Address,on_delete=models.CASCADE, related_name='UserAddress')##


class Likes(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)


class Comments(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    text =models.CharField(max_length=100, blank=False)
    
from django.contrib import admin
from .models import Likes,Posts,User,Comments,Address
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Address)
admin.site.register(User)


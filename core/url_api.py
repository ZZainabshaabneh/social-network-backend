
from django.urls import path

from django.conf.urls import include
from .posts import urls as url_posts
from .users import urls as url_users


urlpatterns=[
    path('',include(url_users)),
    path('',include(url_posts)),
]
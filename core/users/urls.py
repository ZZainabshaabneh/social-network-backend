from django.urls import path
from core.users.views import UserListCreateAPIView




urlpatterns=[
 path('users/',UserListCreateAPIView.as_view()),

]



from rest_framework.response import Response

from core.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from core.users.models import User

class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return  Response(UserSerializer(User.objects.all(),many=True).data)
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from .models import User
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'

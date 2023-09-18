from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Song
from .serializers import SongSerializer


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get('pk'))

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs.get('pk'))

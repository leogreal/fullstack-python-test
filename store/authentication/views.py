from rest_framework import generics

from store.authentication.models import Profile
from store.authentication.serializers import ProfileCreateSerializer


class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

from django.contrib.auth import authenticate, get_user_model

from rest_framework import exceptions
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from store.authentication.models import Profile
from store.authentication.serializers import ProfileCreateSerializer


class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer


class ProfileAuthentication(BasicAuthentication):

    def authenticate(self, request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(
                'No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(
                'Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                'User inactive or deleted.')

        return (user, None)


class ProfileLogin(APIView):
    authentication_classes = (SessionAuthentication, ProfileAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        content = {
            'user': request.user,
            'auth': request.auth,
        }
        return Response(content)

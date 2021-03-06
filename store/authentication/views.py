from django.contrib.auth import login, get_user_model, authenticate

from rest_framework import exceptions
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from store.authentication.models import Profile
from store.authentication.serializers import ProfileCreateSerializer, LoginSerializer


class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        obj = Profile.objects.create_user(
            username=request.data.get('username', None),
            password=request.data.get('password', None),
            name=request.data.get('name', None),
            email=request.data.get('email', None))

        if obj:
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_409_CONFLICT)


class ProfileAuthentication(BasicAuthentication):

    def authenticate(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(
                'No credentials provided.')

        user = Profile.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed(
                'Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                'User inactive or deleted.')

        if user.check_password(password):
            return user

        return None


class ProfileLogin(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        auth = ProfileAuthentication()
        user = auth.authenticate(request)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

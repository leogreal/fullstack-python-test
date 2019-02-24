from rest_framework import serializers
from store.authentication.models import Profile


class ProfileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'name',
            'username',
            'email',
            'password',
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, write_only=True)
    password = serializers.CharField(allow_blank=False, write_only=True)

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

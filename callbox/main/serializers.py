from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Advert


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = (
            'id',
            'title',
            'description',
            'user',
            'date_created',
        )
        read_only_fields = (
            'id',
            'user',
            'date_created',
        )

    user = UserSerializer(many=False, required=False, read_only=True)


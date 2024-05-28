from rest_framework import serializers
from django.contrib.auth import get_user_model

from app_main.models import Note

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }


class NoteSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'body', 'created', 'updated']
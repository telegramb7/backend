from rest_framework import serializers
from .models import User, Anket, Like, Match


class AnketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "age",
            "description",
            "file_unique_id",
            "sex",
        )
        model = Anket


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "partner",
        )
        model = Like


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "who_like",
            "whom_like",
        )
        model = Match


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "id_chat",
        )
        model = User

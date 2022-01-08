from rest_framework import serializers
from .models import User, Anket, Like, Match, Dislike


class AnketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anket
        fields = (
            "id",
            "name",
            "age",
            "description",
            "file_unique_id",
            "sex",
            "user",
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "partner",
        )


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = (
            "id",
            "who_dislike",
            "whom_dislike",
        )


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "who_like",
            "whom_like",
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "id_chat",
            "username",
        )

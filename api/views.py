from rest_framework import viewsets

from .models import User, Anket, Like, Match
from .serializers import (
    UsersSerializer,
    AnketSerializer,
    MatchSerializer,
    LikeSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class AnketViewSet(viewsets.ModelViewSet):
    queryset = Anket.objects.all()
    serializer_class = AnketSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

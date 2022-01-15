from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User, Anket, Like, Match, Dislike
from .serializers import (
    UsersSerializer,
    AnketSerializer,
    MatchSerializer,
    LikeSerializer,
    DislikeSerializer,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from django.db.models import Subquery, Q, OuterRef



class PaginationApi(PageNumberPagination):
    page_size = 3
    max_page_size = 1000000

    def get_paginated_response(self, data):
        return Response(data)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = PaginationApi
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        queryset = User.objects.all()
        id_chat = self.request.query_params.get("id_chat")
        id_user = self.request.query_params.get("id_user")
        if id_chat is not None:
            queryset = queryset.filter(id_chat=id_chat)
        if id_user is not None:
            queryset = queryset.filter(id=id_user)
        return queryset


class AnketViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Anket.objects.all()
    serializer_class = AnketSerializer
    pagination_class = PaginationApi
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        id_chat = self.request.query_params.get('id_chat')
        user = User.objects.filter(id_chat=id_chat).first()
        likes = Like.objects.filter(user=user)
        dislikes = Dislike.objects.filter(who_dislike = user)
        queryset = Anket.objects.exclude(user = user) \
                  .exclude(Q(user__in=Subquery(likes.values('partner_id'))) | Q(user__in=Subquery(dislikes.values('whom_dislike_id'))))
        return queryset

    @action(methods=['GET'], detail=False)
    def me(self, request):
        id_chat = int(request.data.get('id_chat'))
        user = User.objects.filter(id_chat=id_chat).first()
        if not user.anket:
            return Response({"Error":" Not anket"}, status=status.HTTP_400_BAD_REQUEST)
        anket_serializer = AnketSerializer(user.anket)
        return Response(anket_serializer.data, status=status.HTTP_200_OK)


        # queryset = Anket.objects.all()
        # user = self.request.query_params.get("user")
        # if user is not None:
        #     queryset = queryset.filter(user=user)
        # return queryset


class LikeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = PaginationApi
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        queryset = Like.objects.all()
        user = self.request.query_params.get("user")
        partner = self.request.query_params.get("partner")
        if user is not None:
            queryset = queryset.filter(user=user).filter(partner=partner)
        return queryset


class MatchViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    pagination_class = PaginationApi
    permission_classes = [HasAPIKey]


class DislikeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer
    pagination_class = PaginationApi
    permission_classes = [HasAPIKey]

    def get_queryset(self):
        id_chat = self.request.query_params.get('id_chat')
        user = User.objects.filter(id_chat=id_chat).first()
        queryset = Dislike.objects.all()
        who = self.request.query_params.get("who")
        whom = self.request.query_params.get("whom")
        if who is not None:
            queryset = queryset.filter(who_dislike=who)
        if whom is not None:
            queryset = queryset.filter(who_dislike=who).filter(whom_dislike=whom)
        if user is not None:
            queryset = queryset.filter(who_dislike=user)
        return queryset

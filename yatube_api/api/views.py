from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins, filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import AnonRateThrottle
from posts.models import Post, Group, Comment, User

from .permissions import (IsAuthor, UserIsAuthenticated,
                          UserIsAuthenticatedOrReadOnly)
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .throttling import WorkingHoursRateThrottle


class PostViewSet(viewsets.ModelViewSet):
    """Обработка постов"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (UserIsAuthenticatedOrReadOnly, IsAuthor,)
    pagination_class = LimitOffsetPagination
    throttle_classes = (AnonRateThrottle, WorkingHoursRateThrottle)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Информация о группах"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (UserIsAuthenticatedOrReadOnly,)
    throttle_classes = (AnonRateThrottle, WorkingHoursRateThrottle)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """Информация о подписках"""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthor, UserIsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    throttle_classes = (WorkingHoursRateThrottle,)

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Обработка комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthor, UserIsAuthenticatedOrReadOnly,)
    throttle_classes = (AnonRateThrottle, WorkingHoursRateThrottle)

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get("post_id"))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

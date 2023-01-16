from django.shortcuts import render
from rest_framework import permissions

from account.permissions import AnonPermissionOnly,IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)


class PostListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class PostCreateAPIView(CreateAPIView):
    permission_classes = [AnonPermissionOnly]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    permission_classes = [AnonPermissionOnly]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostUpdateAPIView(UpdateAPIView):
    permission_classes = [AnonPermissionOnly,IsOwnerOrReadOnly]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDeleteAPIView(DestroyAPIView):
    permission_classes = [AnonPermissionOnly,IsOwnerOrReadOnly]
    # authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
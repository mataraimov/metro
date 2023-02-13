from rest_framework import viewsets

from apps.account.permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from .serializers import PostSerializer,CategorySerializer
from .models import Post,PostCategory


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer
# class PostListAPIView(ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = PostSerializer
#     def get_queryset(self):
#         qs = Post.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#
# class PostCreateAPIView(CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'
#
#
# class PostUpdateAPIView(UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
#     # authentication_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'
#
#
# class PostDeleteAPIView(DestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
#     # authentication_classes = []
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'


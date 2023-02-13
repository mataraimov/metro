from django.urls import path, include
from rest_framework import routers

from apps.post.views import PostViewSet,PostCategoryView

router=routers.DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'category',PostCategoryView)
urlpatterns = [
    path('',include(router.urls)),
]
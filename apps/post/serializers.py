from rest_framework import serializers

from apps.post.models import Post, PostCategory


class PostSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = ['id', 'name', 'description']
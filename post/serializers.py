from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'body', 'created_at', 'updated_at', 'total_likes')


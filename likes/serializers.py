from post.models import Post
from likes import services as likes_services
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class LikeSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'body',
            'created_at',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)



class FanSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'id',
            'email'
        )

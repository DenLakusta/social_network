from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from six import text_type
from likes.models import Like
from .models import User



UserModel = get_user_model()

class UserLikes(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id',]


class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username','password', 'email', 'tokens')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserAnaliticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'last_visit', 'last_login')




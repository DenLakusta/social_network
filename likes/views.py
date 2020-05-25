from rest_framework import generics
from rest_framework.response import Response
from likes import services
from likes.serializers import LikeSerializer, FanSerializer
from post.models import Post


class PostLikeView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        services.add_like(post, request.user)
        return Response()


class PostUnlikeView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        services.remove_like(post, request.user)
        return Response()


class PostLikesView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = FanSerializer

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        fans = services.get_fans(post)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)



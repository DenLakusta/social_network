from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from likes.models import Like
from .models import User
from .serializers import  UserLikes, UserAnaliticsSerializer, UserSerializer
from .service import LikeFilter


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class LikeAnaliticsView(APIView):

    serializer_class = UserLikes
    filter_backends = (DjangoFilterBackend, )
    filterset_class = LikeFilter

    def get(self, request):
        print(request.GET.get('date_start'))
        likes_filtered = Like.objects.all().count()
        content = {'likes_made in period from {} to {}'.format(request.GET.get('date_start'), request.GET.get('date_to')): likes_filtered}
        return Response(content)


class UserAnalitics(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserAnaliticsSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj


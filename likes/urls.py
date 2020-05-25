from django.urls import path
from likes import views


urlpatterns = [
    path('likes/<int:pk>/', views.PostLikesView.as_view()),
    path('like/<int:pk>/', views.PostLikeView.as_view()),
    path('unlike/<int:pk>/', views.PostUnlikeView.as_view())
]

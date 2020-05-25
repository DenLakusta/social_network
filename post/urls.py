from django.urls import path
from post import views


urlpatterns = [
    path('posts/', views.PostsView.as_view()),
    path('post/<int:pk>/', views.SinglePostView.as_view()),
    path('post/create/', views.CreatePostView.as_view()),
  ]

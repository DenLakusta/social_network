from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.CreateUserView.as_view()),
    path('like_analytics/', views.LikeAnaliticsView.as_view()),
    path('last_activity/', views.UserAnalitics.as_view()),
]

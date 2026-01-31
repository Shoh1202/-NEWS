from django.urls import path
from .views import PostList , DetailPost
urlpatterns=[path("news/",PostList.as_view(),name="news"),
             path("news/<int:pk>/", DetailPost.as_view(), name="news_detail")]


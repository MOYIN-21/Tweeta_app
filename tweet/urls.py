from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from . import views
from .views import CommentViewSet

router = SimpleRouter()
router.register("tweets", views.TweetViewSet, basename='tweets')

comment_router = (routers.NestedDefaultRouter(router, "tweets", lookup ="tweet"))
comment_router.register("comments", CommentViewSet, basename="tweets-comments")


# urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.TweetViewSet.as_view),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    # path('comments/', views.CommentList.as_view()),
    # path('comments/<int:pk>/', views.CommentDetail.as_view())

# ]

urlpatterns = router.urls + comment_router.urls
# print(router.urls)
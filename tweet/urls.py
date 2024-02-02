from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("t", views.TweetViewSet)
router.register("comments", views.CommentViewSet)


# urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.TweetViewSet.as_view),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    # path('<int:pk>/', views.TweetDetail.as_view()),
    # path('comments/', views.CommentList.as_view()),
    # path('comments/<int:pk>/', views.CommentDetail.as_view())

# ]

urlpatterns = router.urls
# print(router.urls)
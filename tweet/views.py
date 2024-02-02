from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView

from .models import Tweet, Comment
from .serializer import TweetSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
# @api_view(["GET", 'POST'])
# def tweet_list(request):
#     if request.method == "GET":
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TweetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(TweetSerializer.data)
#
#
# class TweetList(APIView):
#     def get(self):
#         tweet = Tweet.objects.all()
#         serializer = TweetSerializer(tweet, many=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#     def post(self, request):
#         serializer = TweetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return  Response(serializer.data, status=status.HTTP_201_CREATED)


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# class TweetList(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class TweetDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer


# class CommentList(ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class CommentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer

# class TweetComment()
# class TweetDetails(APIView):
#     def put(self, request, pk):
#         tweet = get_object_or_404(Tweet, pk=pk)
#         serializer = TweetSerializer(tweet,data=request.data )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer)
# @api_view(['GET', 'PUT', 'DELETE'])
# def tweet_details(request, pk):
#     tweet = get_object_or_404(Tweet, pk=pk)
#     if request.method == 'GET':
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = TweetSerializer(tweet, ata=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

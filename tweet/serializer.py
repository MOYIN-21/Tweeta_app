from rest_framework import serializers

from tweet.models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # text = serializers.CharField(max_length=200)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'text', 'last_update']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'commented_on', 'tweet']

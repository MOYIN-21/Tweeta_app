from django.contrib import admin

from tweet.models import Tweet, Comment


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    list_per_page = 10
    search_fields = ['text']
    list_display_links = ['text']


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    list_display = ['comment', 'commented_on', 'tweet', 'id']



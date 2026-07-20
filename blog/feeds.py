from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone

class LatestEntriesFeed(Feed):
    title = "blog latest posts"
    link = "/rss/feed"
    description = "best blog."

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now(),status=1)

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content
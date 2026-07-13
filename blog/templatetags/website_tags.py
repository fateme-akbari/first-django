from django import template
from django.core.paginator import Paginator
from django.utils import timezone
from blog.models import *

register = template.Library()

@register.inclusion_tag("website/website-latest-post.html")
def latestposts(arg=6):
    posts = Post.objects.filter(status=1,
                                published_date__lte=timezone.now()).order_by("-published_date")[:arg]
    return {"posts": posts}
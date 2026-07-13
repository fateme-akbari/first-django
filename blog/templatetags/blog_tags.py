from django import template
from blog.models import *
from django.utils import timezone
from django.core.paginator import Paginator

register = template.Library()
    
@register.simple_tag
def total_post():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).count()
    return posts

@register.inclusion_tag('blog/blog-popular-post.html')
def latestpost(arg=3):
    posts = Post.objects.filter(
        status=1, 
        published_date__lte=timezone.now()).order_by("published_date")[:arg]
    return {"posts": posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategory():
    posts = Post.objects.filter(
        status=1, 
        published_date__lte=timezone.now())
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
        
    return {"categories": cat_dict}


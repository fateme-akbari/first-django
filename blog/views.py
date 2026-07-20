from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.utils.text import Truncator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

def count_views(post):
        post.counted_views += 1
        post.save()
    
def blog_view(request, cat_name=None, username=None, tag_name=None):
    posts = Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if username:
        posts = posts.filter(author__username=username)
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name,])
        
    posts = Paginator(posts, 3) 
    page_number = request.GET.get("page")
    posts = posts.get_page(page_number)
    '''
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    '''
    
    content = {
        "posts": posts,
    }
    return render(request, "blog/blog-home.html", content)

def blog_single_view(request, pid):
    #comments form
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Comment submited")
        else:
            messages.add_message(request, messages.ERROR, "Ooooops!!")
    

    post = get_object_or_404(Post,pk=pid,status=1, published_date__lte=timezone.now())
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    #number of views
    count_views(post)
    
    #previous page - next page
    current_index = list(posts).index(post)
    
    next_post = None
    previous_post = None
    if current_index > 0:
        previous_post = posts[current_index - 1]
    if current_index < len(posts) - 1:
        next_post = posts[current_index + 1]
        
    #show comments
    comments = Comment.objects.filter(post=post, approved=True)
    
    content = {
        "post": post,
        "posts": posts,
        "previous": previous_post,
        "next": next_post,
        "comments": comments,
    }
    return render(request, "blog/blog-single.html", content)

#merge this function to blog_view
'''def blog_category(request, cat_name):
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now(),
        category__name=cat_name
    )
    
    content = {
        "posts": posts
    }
    
    return render(request, "blog/blog-home.html", content)
'''

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if request.method == "GET":
        posts = posts.filter(content__contains=request.GET.get('s'))
    content = {
        "posts": posts
    }
    return render(request, "blog/blog-home.html", content)
    
def test_read(request):
    posts = Post.objects.all()
    print(posts)
    content = {
        "posts": posts,
        #"title": title
    }
    return render(request, "read-data.html", content)
from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("post-<int:pid>", blog_single_view, name="single"),
    path("category/<str:cat_name>", blog_view, name="category"),
    path("author/<str:username>", blog_view, name="author"),
    path("search/", blog_search, name="search"),
    path("test", test_read)
]
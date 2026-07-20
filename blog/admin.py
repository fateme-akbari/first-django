from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title', 'status', 'counted_views', 'published_date')
    list_filter = ('status', 'author')
    ordering = ('created_date',)
    search_fields = ('content', 'title')
    summernote_fields = ('content',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'empty'
    search_fields = ('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ["name", "subject", "approved", "created_date"]
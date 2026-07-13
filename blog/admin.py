from django.contrib import admin
from blog.models import *

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title', 'status', 'counted_views', 'published_date')
    list_filter = ('status', 'author')
    ordering = ('created_date',)
    search_fields = ('content', 'title')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'empty'
    search_fields = ('name',)
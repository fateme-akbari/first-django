from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to="blog/", default="default.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    category = models.ManyToManyField(Category)
    ## Use __str__() to display the title instead of the object ID in the Django admin panel.
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['created_date']
        
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    
    

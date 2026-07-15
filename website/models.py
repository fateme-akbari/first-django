from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created_date']

class NewsLetterModel(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
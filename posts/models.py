from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    category = models.CharField(max_length=20) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title
    
class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
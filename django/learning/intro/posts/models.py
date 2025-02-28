from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


class Post(models.Model):
    title   = models.CharField(max_length=100)
    body    = models.TextField()
    slug    = AutoSlugField(populate_from='title', unique=True, editable=True)
    date    = models.DateTimeField(auto_now_add=True)
    banner  = models.ImageField(default="placeholder.jpg", blank=True)
    author  = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.title

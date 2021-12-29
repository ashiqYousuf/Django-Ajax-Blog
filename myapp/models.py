from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    likes=models.PositiveIntegerField(default=0)
    dislikes=models.PositiveIntegerField(default=0)
    slug=models.SlugField(max_length=100)
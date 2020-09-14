from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/posts/')
    text = HTMLField()
    data = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

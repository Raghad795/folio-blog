from django.db import models
from django.contrib.auth.hashers import make_password, identify_hasher

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.username)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
        )
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

from django.db import models
from ManageVisitor.models import Visitor
from PostManagement.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    Comment_description = models.TextField(max_length=5000)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username




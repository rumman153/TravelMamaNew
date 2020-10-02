from django.db import models
from ManageVisitor.models import Visitor

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50,
                                     choices=(('Regions','Regions'),
                                              ('Popular Places', 'Popular Places'),
                                              ('Blog', 'Blog')),
                                     default='Blog')
    Post_tags = models.CharField(max_length=200)
    Post_image= models.ImageField(null='true')
    Post_description = models.TextField(max_length=100000)

    User = models.ForeignKey(User, on_delete=models.CASCADE,null='true')

    def __str__(self):
        return self.Post_title

# operationalerror no such table
# python manage.py migrate --run-syncdb
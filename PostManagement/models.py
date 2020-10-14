from django.db import models
from ManageVisitor.models import Visitor
from django.contrib.auth.models import User


class Review(models.Model):
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=10, choices = RATING_OPTIONS, default='4')
    comment = models.TextField(blank=True, null=True)

    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#
#     description = models.TextField()
#
#     def __str__(self):
#         return self.description


class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50,
                                     choices=(('Travel Blog', 'Travel Blog'),
                                              ('Travel Guide', 'Travel Guide'),
                                              ('Travel Package', 'Travel Package')),
                                     default='Travel Blog')
    Post_tags = models.CharField(max_length=200)
    Post_image= models.ImageField(null='true')
    Post_description = models.TextField(max_length=100000)

    User = models.ForeignKey(User, on_delete=models.CASCADE,null='true')

    reviews = models.ManyToManyField(Review)


    def __str__(self):
        return self.Post_title

# operationalerror no such table
# python manage.py migrate --run-syncdb



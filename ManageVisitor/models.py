from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Visitor(models.Model):
    Visitor_name = models.CharField(max_length=100)
    Visitor_email = models.EmailField(max_length=100)
    Gender = models.CharField(max_length=50,
                                     choices=(('Male', 'Male'),
                                              ('Female', 'Female'),
                                              ),
                                     default='Male')
    Visitor_picture = models.ImageField(upload_to='images/Visitor_profile/', default=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Visitor_name



from django.db import models

# Create your models here.
class Admin(models.Model):
    Admin_name = models.CharField(max_length=100)
    Admin_profile = models.ImageField(upload_to='images/Admin_profile/', default=1)
    Admin_email = models.EmailField(max_length=100,unique=True)
    Admin_contact = models.CharField(max_length= 15,unique=True)

    def __str__(self):
        return self.Admin_name

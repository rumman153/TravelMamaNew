
from django.contrib import admin

# Register your models here.
from .models import Post, Review


admin.site.register([Post, Review])

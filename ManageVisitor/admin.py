from django.contrib import admin

# Register your models here.
from .models import Visitor


admin.site.register([Visitor])
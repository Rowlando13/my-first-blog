from django.contrib import admin
#why .models
from .models import Post

# Register your models here.
#registering Post class created in model.py
admin.site.register(Post)

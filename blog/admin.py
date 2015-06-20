from django.contrib import admin # allows to add, edit, & delete posts
from .models import Post

admin.site.register(Post) # makes post visible on admin page
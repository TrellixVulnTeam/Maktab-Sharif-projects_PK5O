from django.contrib import admin

from post.models import Category, Comment, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

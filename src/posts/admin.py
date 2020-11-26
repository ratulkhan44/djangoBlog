from django.contrib import admin
from .models import Post, PostView, Like, Comment, User

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)

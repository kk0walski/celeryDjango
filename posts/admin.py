from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['id', 'platform', 'user', 'link', 'created_at', 'text', 'title']

admin.site.register(Post, PostAdmin)

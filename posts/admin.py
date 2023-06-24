from django.contrib import admin

# Register your models here.
from .models import Post , Author


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'puplish_date']
    list_filter = ['author', 'tags', 'puplish_date']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
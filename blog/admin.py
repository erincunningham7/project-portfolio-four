from django.contrib import admin
# import blogpost model
from .models import BlogPost, Comment


@admin.register(BlogPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
    prepopulated_fields = {'slug': ('title',), }
    list_filter = ('date_created', 'status')
    search_fields = ('title_startswith',)

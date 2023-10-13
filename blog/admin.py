from django.contrib import admin
# import blogpost model
from .models import BlogPost


@admin.register(BlogPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass

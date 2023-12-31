from django.shortcuts import render
from django.views import generic
from .models import BlogPost


class BlogListView(generic.ListView):
    model = BlogPost
    # queryset = BlogPost.objects.filter(
    #    status=POSTED).order_by('-date_created')
    paginate_by = 3
    template_name = 'index.html'

    def get_queryset(self):
        # Filter only 'Posted' blog posts
        queryset = BlogPost.objects.filter(status='Posted')
        return queryset

from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostsListView(ListView):
    model = Post
    template_name = 'community/posts_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
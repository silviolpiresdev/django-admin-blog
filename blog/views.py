from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post



class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "lista_posts.html"
    
    


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "lista_post.html"
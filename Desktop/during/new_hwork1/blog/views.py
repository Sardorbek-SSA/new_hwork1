from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post"
    paginate = 6    
    
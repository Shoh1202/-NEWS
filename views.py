from django.db.models.functions import LastValue
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model=Post
    ordering='-time_add'
    template_name='news/news_list.html'
    context_object_name ='news_list'

class DetailPost(DetailView):
    model=Post
    template_name = "news/news_detail.html"
    context_object_name = "news"

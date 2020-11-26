from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment

# Create your views here.


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post

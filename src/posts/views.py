from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment
from .forms import PostForm,CommentForm

# Create your views here.


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    form_class=PostForm
    model = Post
    success_url='/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context


class PostDetailView(DetailView):
    model = Post

    def post(self,*args,**kwargs):
        form=CommentForm(self.request.POST)
        post=self.get_object()
        if form.is_valid():
            comment=form.instance
            comment.user=self.request.user
            comment.post=post
            comment.save()
            return redirect('detail',slug=post.slug)
        return redirect('detail',slug=self.get_object().slug)   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form':CommentForm()
        })
        return context



    def get_object(self,**kwargs):
        object=super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user,post=object)
        return object
    



class PostUpdateView(UpdateView):
    form_class=PostForm
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url='/'


def like(request,slug):
    post= get_object_or_404(Post,slug=slug)
    like_qs=Like.objects.filter(user=request.user,post=post)  
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail',slug=slug)
    Like.objects.create(user=request.user,post=post)
    return redirect('detail',slug=slug)          

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostList(LoginRequiredMixin,generic.ListView):      #html: post_list   context: object_list or post_list
    model = Post
    login_url = '/admin/login' 


class PostDetail(generic.DetailView):      #html: post_detail   context: object or post
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = ['title', 'puplish_date', 'content', 'author', 'image', 'tags']
    success_url = '/blog/'


class PostEdit(generic.UpdateView):
    model = Post
    fields = ['title', 'puplish_date', 'content', 'author', 'image', 'tags']
    success_url = '/blog/'
    template_name = 'posts/edit.html'



class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/blog/'



def delete_post(request, post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog/')
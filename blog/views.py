from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
	model = Post
	fields = '__all__'
	template_name = 'blog/post_create.html'


class BlogUpdateView(UpdateView):
	model = Post
	fields = ('title', 'body')
	template_name = 'blog/post_update.html'


class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')

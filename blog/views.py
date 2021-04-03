from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


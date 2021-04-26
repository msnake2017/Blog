from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
	model = Article
	template_name = 'articles/article_list.html'
	context_object_name = 'articles'


class ArticleDetailView(LoginRequiredMixin, DetailView):
	model = Article
	template_name = 'articles/article_detail.html'
	context_object_name = 'article'


class ArticleEditView(LoginRequiredMixin, UpdateView):
	model = Article
	template_name = 'articles/article_edit.html'
	fields = ('title', 'body')

	def dispatch(self, request, *args, **kwargs):
		article = self.get_ob


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
	model = Article
	template_name = 'articles/article_delete.html'
	success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'articles/article_create.html'
	fields = ('title', 'body')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(ArticleCreateView, self).form_valid(form)

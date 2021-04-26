from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article


class ArticleListView(ListView):
	model = Article
	template_name = 'articles/article_list.html'
	context_object_name = 'articles'


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articles/article_detail.html'
	context_object_name = 'article'


class ArticleEditView(UpdateView):
	model = Article
	template_name = 'articles/article_edit.html'
	fields = ('title', 'body')


class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'articles/article_delete.html'
	success_url = reverse_lazy('article_list')


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'articles/article_create.html'
	fields = ('title', 'body')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(ArticleCreateView, self).form_valid(form)

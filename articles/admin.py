from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.StackedInline):
	model = Comment
	list_display = ('author', 'comment')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date')
	inlines = [CommentInline]

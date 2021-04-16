from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    date = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name=_('date'))
    author = models.ForeignKey(
                                get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name=_('author'))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])

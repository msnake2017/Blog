from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class Post(models.Model):

    author = models.ForeignKey(get_user_model(), verbose_name=_('author'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('post_detail', args=[self.id])

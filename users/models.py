from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name=_('age'), null=True, blank=True)

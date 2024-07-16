from django.db import models


from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(
        max_length=50, null=False, verbose_name=_('Username'))
    name = models.CharField(
        max_length=50, null=True, verbose_name=_('Name'))
    password = models.CharField(
        max_length=50, null=False, verbose_name=_('Password'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created date'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated date'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

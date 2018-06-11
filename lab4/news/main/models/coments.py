from django.db import models
from main.models.news import News
from django.contrib.auth.models import User

class Coments(models.Model):

    class Meta:
        db_table = 'comments'
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'
        ordering = ['pubtime']

    new = models.ForeignKey(News, editable=False, on_delete=models.CASCADE)

    user = models.ForeignKey(
                             User,
                             verbose_name='Пользователь',
                             editable=False,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True
                            )

    text = models.TextField(verbose_name='Коментарий')

    pubtime = models.DateTimeField(
                                   auto_now_add=True,
                                   editable=False,
                                   verbose_name='Дата коментирования'
                                   )

    def __str__(self):
        return  '{} к новости "{}" ({:%d.%m.%Y %H:%M})'\
                .format(self.user, self.new, self.pubtime)

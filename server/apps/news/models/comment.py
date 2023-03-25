from datetime import date

from django.db import models


class Comment(models.Model):
    create_date = models.DateField(
        default=date.today,
        verbose_name='Дата создания'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    news = models.ForeignKey(
        to='news.news',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return f'{self.author} {self.text}'

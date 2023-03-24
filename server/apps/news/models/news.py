from datetime import date

from django.db import models


class News(models.Model):
    create_date = models.DateField(
        default=date.today,
        verbose_name='Дата создания'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return f'{self.author} {self.title}'

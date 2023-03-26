from django.db import models


class Like(models.Model):
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пользователь',
    )
    news = models.ForeignKey(
        to='news.news',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Новость'
    )

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self) -> str:
        return f'{self.user} {self.news}'

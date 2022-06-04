from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Сообщество'
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        unique=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title

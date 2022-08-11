from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, F, Q, UniqueConstraint


class User(AbstractUser):
    """
    Модель пользователя.
    """
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта пользователя',
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        unique=True,
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль пользователя',
        blank=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = [
            UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            )
        ]

    def __str__(self):
        return self.email


class Follow(models.Model):
    """
    Модель подписок пользователей на авторов.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='На кого подписались',
    )

    class Meta:
        verbose_name = 'Подписки на пользователей'
        verbose_name_plural = 'Подписку на пользователя'
        constraints = [
            UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            ),
            CheckConstraint(
                name='unique_object_following',
                check=~Q(user=F('following')),
            )
        ]

    def __str__(self) -> str:
        return self.user.username

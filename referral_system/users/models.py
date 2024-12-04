from django.db import models
from django.utils.crypto import get_random_string


class User(models.Model):
    """Модель пользователя."""

    user_invite_code = models.CharField(
        max_length=6,
        verbose_name='Инвайт-код пользователя',
        unique=True,
        blank=True,
        null=True
    )
    friend_invite_code = models.CharField(
        max_length=6,
        verbose_name='Инвайт-код друга',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона',
        unique=True
    )
    code = models.IntegerField(
        verbose_name='Код входа',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.phone_number}'

    def save(self, *args, **kwargs):
        if not self.user_invite_code:
            self.user_invite_code = get_random_string(
                6, allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789'
                )
        super().save(*args, **kwargs)

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Проверяем, что это новый пользователь или пароль был изменен.
        old_user = User.objects.get(pk=self.pk)
        if self._state.adding or self.password != old_user.password:
            # Хешируем пароль.
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email}, {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

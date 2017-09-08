import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuario', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w]+$'), 'O nome de usuario so pode conter letras e digitos', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome Completo', max_length=100, blank=True)
    is_active = models.BooleanField('Esta ativo?', blank=True, default=True)
    is_staff = models.BooleanField('E da equipe?', blank=True, default=False)
    data_joined = models.DateTimeField('Data de Entada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class SenhaReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuario',
        related_name='resets'
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.criado_em)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-criado_em']

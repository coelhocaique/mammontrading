from django.db import models
from conta.models import User
from django.conf import settings


# Create your models here.

class Robo(models.Model):
    TIPO = {
        (0, 'Conservador'),
        (1, 'Moderado'),
        (2, 'Arrojado'),
    }
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug', max_length=100)
    imagem = models.ImageField(upload_to='imagens', verbose_name='Imagem')
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=6)
    descricao = models.TextField('Descricao')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    tipo = models.IntegerField('Tipo', choices=TIPO, default=0, blank=True)

    def __str__(self):
        return self.nome;

    @models.permalink
    def get_absolute_url(self):
        return ('robo:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Robo'
        verbose_name_plural = 'Robos'
        ordering = ['nome']


class RoboComprado(models.Model):
    STATUS_COMPRA = {
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='robos')
    robo = models.ForeignKey(Robo, verbose_name='Robo', related_name='compras')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    status = models.IntegerField('Situacao', choices=STATUS_COMPRA, default=0, blank=True)
    name_mt5 = models.CharField('Nome MT5', max_length=50)
    codigo = models.FileField(upload_to='arquivos', blank=True, null=True)

    def ativar(self):
        self.status = 1;
        self.save()

    def cancelar(self):
        self.status = 2;
        self.save()

    def esta_ativo(self):
        return self.status == 1

    def __str__(self):
        return self.user.name + " & " + self.robo.nome

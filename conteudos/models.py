from django.db import models
from tinymce.models import HTMLField


class Video(models.Model):
    titulo = models.CharField('Titulo', max_length=255)
    slug = models.SlugField('Slug', primary_key=True)
    descricao = models.TextField('Descricao')
    endereco = models.TextField('Link')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

class Artigo(models.Model):
    titulo = models.CharField('Titulo', max_length=255)
    slug = models.SlugField('Slug', primary_key=True)
    imagem = models.ImageField(upload_to='imagens', verbose_name='Imagem', blank=True)
    descricao = models.TextField('Descricao')
    texto = HTMLField('Texto')
    endereco_original = models.CharField('Link', max_length=255)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.titulo

    @models.permalink
    def get_absolute_url(self):
        return ('conteudo:artigo.details', (), {'slug': self.slug})




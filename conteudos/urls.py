from django.views.generic import list, detail
from django.conf.urls import url
from .models import Artigo, Video

app_name = 'conteudo'
urlpatterns = [
    url(r'^artigos/$', list.ListView.as_view(model=Artigo), name='artigo.index'),
    url(r'^artigos/(?P<pk>[\w_-]+)/$', detail.DetailView.as_view(model=Artigo), name='artigo.details'),
    url(r'^videos/$', list.ListView.as_view(model=Video), name='video.index'),
    url(r'^videos/(?P<pk>[\w_-]+)/$', detail.DetailView.as_view(model=Video), name='video.details')
]
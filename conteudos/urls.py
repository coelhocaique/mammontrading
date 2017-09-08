from django.views.generic import list, detail
from django.conf.urls import url
from .models import Artigo, Video
from .views import artigo_list

app_name = 'conteudo'
urlpatterns = [
    url(r'^artigos/$', artigo_list, name='artigo.index'),
    url(r'^artigos/(?P<slug>[\w_-]+)/$', detail.DetailView.as_view(model=Artigo), name='artigo.details'),
    url(r'^videos/$', list.ListView.as_view(model=Video), name='video.index'),
    url(r'^videos/(?P<slug>[\w_-]+)/$', detail.DetailView.as_view(model=Video), name='video.details')
]

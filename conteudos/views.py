from django.views import generic

from conteudos.models import Artigo


class ArtigoListView(generic.ListView):
    model = Artigo
    ordering = ['-criado_em']


artigo_list = ArtigoListView.as_view()

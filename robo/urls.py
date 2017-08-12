from django.views.generic import list, detail
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .models import Robo
from .views import comprar_robo, adicionar_metatrade

app_name = 'robo'
urlpatterns =[
    url(r'^$', list.ListView.as_view(model=Robo), name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', detail.DetailView.as_view(model=Robo), name='details'),
    url(r'^compra/(?P<slug>[\w_-]+)/$', comprar_robo, name='compra'),
    url(r'^(?P<pk>[\w_-]+)/metatrade$', adicionar_metatrade, name='metatrade'),
]


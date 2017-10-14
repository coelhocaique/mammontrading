from django.conf.urls import url
from .views import api
from .views import ativos
from .views import tipos_saida

app_name = 'client'

urlpatterns = [
   url(r'^api/([0-9]{1})/([0-9]{1})/([0-9]+)$', api, name='api'),
   url(r'^api/ativos/$', ativos, name='ativos'),
   url(r'^api/tipos-saida/$', tipos_saida, name='tipos_saida')
]
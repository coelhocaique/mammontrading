from django.conf.urls import url
from .views import operacao

app_name = 'metatrade'

urlpatterns = [
   url(r'^operacao/$', operacao, name='operacao')
]
from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns =[
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contato, name='contato')
]
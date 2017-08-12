from django.conf.urls import  url
from django.contrib.auth import views
from .views import *

app_name = 'conta'
urlpatterns = [
    url(r'^$', dashboard, name='index'),
    url(r'^login/$', views.login, {'template_name': 'conta/login.html'}, name='login'),
    url(r'^cadastre/$', register, name='cadastre'),
    url(r'^logout/$', views.logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^robos/$', robos, name='robos'),
    url(r'^nova-senha/$', senha_reset, name='senha_reset'),
    url(r'^editar/$', editar, name='editar'),
    url(r'^editar-senha/$', editar_senha, name='editar-senha'),
    url(r'^nova-senha/(?P<key>\w+)/$',senha_reset_confirmar ,name='password_reset_confirm')
]
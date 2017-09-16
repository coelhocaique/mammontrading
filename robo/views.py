from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Robo, RoboComprado
from core.utils import generate_hash_key


# Create your views here.

@login_required
def comprar_robo(request, slug):
    if request.method == 'POST':
        robo = get_object_or_404(Robo, slug=slug)
        RoboComprado.objects.create(user=request.user, robo=robo)
    return redirect('conta:robos')


def adicionar_metatrade(request, pk):
    robo_comprado = get_object_or_404(RoboComprado, pk=pk, user=request.user)
    robo_comprado.name_mt5 = request.POST.get('mt5')
    robo_comprado.save()
    msg = 'Login alterado com sucesso'
    messages.add_message(request, messages.INFO, msg)
    return redirect('conta:robos')


def ativar_robo(request, pk):
    robo_comprado = get_object_or_404(RoboComprado, pk=pk, user=request.user)
    robo_comprado.ativar()
    return redirect('conta:robos')


def gerar_token(request, pk):
    robo_comprado = get_object_or_404(RoboComprado, pk=pk, user=request.user)
    robo_comprado.token = generate_hash_key(robo_comprado.pk)
    robo_comprado.save()
    return redirect('conta:robos')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Robo, RoboComprado

# Create your views here.

@login_required
def comprar_robo(request, slug):
   robo = get_object_or_404(Robo, slug=slug)
   RoboComprado.objects.create(user=request.user, robo=robo)
   return render(request, 'conta/robos.html')

def adicionar_metatrade(request, pk):
    robo_comprado = get_object_or_404(RoboComprado, pk=pk, user=request.user)
    robo_comprado.name_mt5 = request.POST.get('mt5')
    robo_comprado.save()
    msg = 'Login alterado com sucesso'
    messages.add_message(request, messages.INFO, msg)
    return redirect('conta:robos')

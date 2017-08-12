from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SenhaResetForm, EditarContaForm
from .models import SenhaReset

# Create your views here.
def register(request):
    template_name = 'conta/registro.html'
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user = authenticate(username=user.username,
                                password=form.cleaned_data['password1'])
        login(request, user)
        return redirect('core:home')

    context = {}
    context['form'] = form
    return render(request, template_name, context)

def senha_reset(request):
    template_name = 'conta/senha_reset.html'
    context = {}
    form = SenhaResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
        # enviar e-mail
    context['form'] = form
    return render(request, template_name, context)

def senha_reset_confirmar(request, key):
    template_name = 'conta/senha_reset_confirmar.html'
    context = {}
    reset = get_object_or_404(SenhaReset, key=key)
    if reset.confirmed == True:
        context['key_usada'] = True
        return render(request, template_name, context)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        reset.confirmed = True
        reset.save()
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'conta/minha_conta.html'
    return render(request, template_name)

@login_required
def robos(request):
    template_name = 'conta/robos.html'
    return render(request, template_name)

@login_required
def editar(request):
    template_name = 'conta/editar.html'
    context = {}
    form = EditarContaForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        msg = 'Dados alterados com sucesso'
        messages.add_message(request, messages.INFO, msg)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def editar_senha(request):
    template_name = 'conta/editar_senha.html'
    context = {}
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        msg = 'A sua senha foi alterada com sucesso'
        messages.add_message(request, messages.INFO, msg)
    context['form'] = form
    return  render(request, template_name, context)

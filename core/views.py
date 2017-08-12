from django.shortcuts import render
from .forms import FaleConosco

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def contato(request):
    context = {}
    form = FaleConosco(request.POST or None)
    if form.is_valid():
        context['is_valid'] = True
        form.send_email()
        form = FaleConosco()

    context['form'] = form
    return render(request, 'core/contato.html', context)

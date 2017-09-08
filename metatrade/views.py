from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def operacao(request):
    message = "{0}\n{1}".format(request.method, request.POST)
    return HttpResponse(message)

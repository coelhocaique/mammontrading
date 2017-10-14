from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from client.models import Utils
import client.trade.neural_networks as nn
import json

@csrf_exempt
def api(request, ativo, tipo, qtd):
    if request.method == 'GET':
        if int(ativo) not in Utils.ATIVOS.keys():
            raise ValueError('Ativo inválido')

        if int(tipo) not in Utils.TIPO_SAIDA.keys():
            raise ValueError('Tipo de saída inválido')

        lstm = nn.LSTM(ativo=ativo,
                       qtd_saidas=qtd,
                       tipo_saida=tipo)

        predictions = lstm.predict()

    return HttpResponse(predictions)

@csrf_exempt
def ativos(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(Utils.ATIVOS))

@csrf_exempt
def tipos_saida(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(Utils.TIPO_SAIDA))
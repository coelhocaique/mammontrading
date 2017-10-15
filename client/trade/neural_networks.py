from client.models import Utils
import json

class LSTM:
    def __init__(self,
                 ativo,
                 qtd_saidas,
                 tipo_saida):
        self.ativo = int(ativo)
        self.qtd_saidas = int(qtd_saidas)
        self.tipo_saida = int(tipo_saida)

    def predict(self):
        model_name = Utils.ATIVOS[self.ativo] + '_' + Utils.TIPO_SAIDA[self.tipo_saida]
        print ('Loading model to predict: %s' % model_name)

        # load_model
        # model.predict
        predictions = range(0, self.qtd_saidas)

        return predictions

class DTO:
    def __init__(self,
                 number_prediction,
                 prediction):
        self.n = number_prediction
        self.prediction = prediction

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
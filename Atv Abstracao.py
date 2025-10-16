from abc import ABC, abstractmethod

class pagamento(ABC):
    @abstractmethod
    def __init__(self,valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass 

class cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self):
        pass

class pagamento_cartao(pagamento, cancelavel):
    def processar_pagamento(self):
        return f'pagando {self.valor} com cartão de crédito.'

class boleto_bancario(pagamento):
    def pagar(self, valor):
        print(f'Pagando {valor} com boleto bancário.')
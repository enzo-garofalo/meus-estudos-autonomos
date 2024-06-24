class Bank:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

class Agency(Bank):
    def __init__(self, nome, endereco, numero):
        self._numero = numero
        super().__init__(nome, endereco)
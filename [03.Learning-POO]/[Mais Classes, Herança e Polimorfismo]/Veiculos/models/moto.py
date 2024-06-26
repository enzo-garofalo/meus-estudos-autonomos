from models.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
    
    def ligar(self):
       self._ligado = True
       return self._ligado

    def __str__(self):
        return super().__str__() + f'\n--Tipo: {self._tipo}'

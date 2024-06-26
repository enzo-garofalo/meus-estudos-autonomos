from models.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        self._num_portas = num_portas

        super().__init__(marca, modelo)
    
    def ligar(self):
       self._ligado = True
       return self._ligado

    def __str__(self):
        return super().__str__() + f'\n--Núm. de portas: {self._num_portas}'


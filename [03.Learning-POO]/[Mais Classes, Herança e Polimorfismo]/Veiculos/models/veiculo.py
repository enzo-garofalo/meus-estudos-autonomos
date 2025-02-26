from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    def __str__(self):
        return f'Marca: {self._marca}\n--Modelo: {self._modelo}\n--Estado: {self.ligado}'

    @abstractclassmethod
    def ligar():
        pass

    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'

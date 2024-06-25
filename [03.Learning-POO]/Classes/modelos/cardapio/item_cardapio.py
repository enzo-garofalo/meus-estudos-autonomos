from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
      self._nome = nome
      self._preco = preco

    # Todas as clases derivadas precisam dessa aplicação para funcionar, mas a classe mão 
    # não precisa saber da funcionalidade dessa função
    @abstractclassmethod
    def aplicar_desconto(self):
      pass


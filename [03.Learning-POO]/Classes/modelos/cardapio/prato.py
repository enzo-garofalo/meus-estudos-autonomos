from modelos.cardapio.item_cardapio import ItemCardapio

#Com isso fazemos com que a classe Prato herde os atributos e métodos da classe ItemCardapio - Classe mãe
#Mantemos uma linha de raciocínio para todos os outras classes
class Prato(ItemCardapio): 
   def __init__(self, nome, preco, descricao):
      self._descricao = descricao
      # Com isso é permitido acessar as informações de outra classe
      super().__init__(nome, preco)
   
   def aplicar_desconto(self):
      self._preco -= (self._preco*0.05)
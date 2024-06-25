from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        self._tamanho = tamanho
        super().__init__(nome, preco)
    
    def aplicar_desconto(self):
        self._preco -= (self._preco*0.08)
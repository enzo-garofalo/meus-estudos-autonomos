from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_1 = Restaurante('Seu Mário', 'Gourmet', 300)
restaurante_2 = Restaurante('Seu Joaquim', 'Italiano', 300)
restaurante_3 = Restaurante('Temakeria.Com', 'Ruim', 300)

bebida = Bebida('Suco de melancia', 5.00, 'Grande')
prato  = Prato('Strogonoff', 2.00, 'Strogonoff de filé mignon')

bebida.aplicar_desconto()
prato.aplicar_desconto()

restaurante_1.adicionar_no_cardapio(bebida)
restaurante_1.adicionar_no_cardapio(prato)

def main():
    restaurante_1.consultar_cardapio

if __name__ == '__main__':
    main()
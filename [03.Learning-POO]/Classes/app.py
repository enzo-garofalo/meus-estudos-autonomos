from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_1 = Restaurante('Seu Mário', 'Gourmet', 300)
restaurante_2 = Restaurante('Seu Joaquim', 'Italiano', 300)
restaurante_3 = Restaurante('Temakeria.Com', 'Ruim', 300)

bebida = Bebida('Suco de melancia', 9.90, 'Grande')
prato  = Prato('Strogonoff', 52.90, 'Strogonoff de filé mignon')

def main():
    print(bebida._nome)
    print(prato._nome)

if __name__ == '__main__':
    main()
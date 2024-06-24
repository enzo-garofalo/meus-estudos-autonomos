from modelos.restaurante import Restaurante

restaurante_1 = Restaurante('Seu Mário', 'Gourmet', 300)
restaurante_2 = Restaurante('Seu Joaquim', 'Italiano', 300)
restaurante_3 = Restaurante('Temakeria.Com', 'Ruim', 300)

restaurante_2.receber_avaliacao('Gui',5 )
restaurante_2.receber_avaliacao('Lais', 5)
restaurante_2.receber_avaliacao('Emy', 5)

def main():
  Restaurante.lista_restaurantes()



if __name__ == '__main__':
  main()
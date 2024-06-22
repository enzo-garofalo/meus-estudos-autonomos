class Restaurante():
  restaurantes = []
  
  # Self é a referencia atual da instância que está chamando
  def __init__(self, nome, categoria, ativo, capacidade, nota_avaliacao):
      self.nome = nome
      self.categoria = categoria
      self.ativo = ativo
      self.capacidade = capacidade
      self.nota_avaliacao = nota_avaliacao

      Restaurante.restaurantes.append(self)
  
  # STR é uma maneira de retornar o objeto em formato de texto
  def __str__(self):
      return f'{self.nome}\n \
               {self.categoria}\n \
               Ativo : {self.ativo}\n \
               Capacidade: {self.capacidade} Pessoas\n \
               Nota: {self.nota_avaliacao}'

  def lista_restaurantes():
     for restaurante in Restaurante.restaurantes:
        print(restaurante)
        

restaurante1 = Restaurante('Seu Mário', 'Brasileiro', True, 100, '5 Estrelas')
restaurante1 = Restaurante('Seu Joaquim', 'Italiano', True, 150, '5 Estrelas')
restaurante1 = Restaurante('Temakeria.com', 'Ruim', True, 300, '2 Estrelas')

Restaurante.lista_restaurantes()
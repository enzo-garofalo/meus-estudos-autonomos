class Restaurante():
  restaurantes = []
  # Self é a referencia atual da instância que está chamando
  def __init__(self, nome, categoria, capacidade, nota_avaliacao):
      # Com o '_' o atributo se torna protegido/privado, ou seja, ele não é modificavel pelo user ou por outras classes  
      self._nome = nome.title()
      self._categoria = categoria
      self._capacidade = capacidade
      self._nota_avaliacao = nota_avaliacao
      self._ativo = False

      Restaurante.restaurantes.append(self)
  # STR é uma maneira de retornar o objeto em formato de texto
  def __str__(self):
      return   f'{self._nome}\n' \
               f'               Categoria: {self._categoria}\n' \
               f'               Ativo : {self.ativo}\n' \
               f'               Capacidade: {self._capacidade} Pessoas\n' \
               f'               Nota: {self._nota_avaliacao}'
  #Indicando um método da classe   
  @classmethod
  def lista_restaurantes(cls):
     for restaurante in cls.restaurantes:
        print(restaurante)
  
  #Muda como o atributo vai ser lido/impresso, poderia fazer cálculos aqui   
  @property
  def ativo(self):
     return 'Ativo ✅' if self._ativo else 'Desativado ❎'
  
  def alternar_estado(self):
     self._ativo = not self._ativo


restaurante1 = Restaurante('seu Mário', 'Brasileiro', 100, '5 Estrelas')
restaurante1.alternar_estado()

restaurante2 = Restaurante('Seu Joaquim', 'Italiano',  150, '5 Estrelas')
restaurante3 = Restaurante('Temakeria.com', 'Ruim',  300, '2 Estrelas')

Restaurante.lista_restaurantes()
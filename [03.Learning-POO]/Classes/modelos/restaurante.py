from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

class Restaurante:
   restaurantes = []
   # Self é a referencia atual da instância que está chamando
   def __init__(self, nome, categoria, capacidade):
      # Com o '_' o atributo se torna protegido/privado, ou seja, ele não é modificavel pelo user ou por outras classes  
      self._nome = nome.title()
      self._categoria = categoria
      self._capacidade = capacidade
      self._avaliacao = []
      self._ativo = False
      self._cardapio = []

      Restaurante.restaurantes.append(self)
   # STR é uma maneira de retornar o objeto em formato de texto
   def __str__(self):
      return   f'{self._nome}\n' \
               f'               Categoria: {self._categoria}\n' \
               f'               Ativo : {self.ativo}\n' \
               f'               Capacidade: {self._capacidade} Pessoas\n' \
               f'               Nota: {self.media_avaliacoes}'
   #Indicando um método da classe   
   @classmethod
   def lista_restaurantes(cls):
     for restaurante in cls.restaurantes:
        print(restaurante)

   @property
   def consultar_cardapio(self):
      print(f'\n\tCardapio do {self._nome}\n'+'-'*40)
      for i, item in enumerate(self._cardapio, start=1):
         if hasattr(item, '_descricao'):
            mensagem_prato = f'{i}. Nome: {item._nome}\n   -Preco: R$ {item._preco}\n   -Descrição: {item._descricao}'
            print(mensagem_prato)
         else:
            mensagem_bebida = f'{i}. Nome: {item._nome}\n   -Preco: R$ {item._preco}\n   -Tamanho: {item._tamanho}'
            print(mensagem_bebida)
         print('-'*40)
   #Muda como o atributo vai ser lido/impresso, poderia fazer cálculos aqui   
   @property
   def ativo(self):
     return 'Ativo ✅' if self._ativo else 'Desativado ❎'
  
   def alternar_estado(self):
     self._ativo = not self._ativo

   def receber_avaliacao(self, cliente, nota):
      if 0 < nota <= 5:
         avaliacao = Avaliacao(cliente, nota)
         self._avaliacao.append(avaliacao)
   
   @property
   def media_avaliacoes(self):
      if not self._avaliacao:
         return '-'
      
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      qtd_de_notas = len(self._avaliacao)
      media = round(soma_das_notas/qtd_de_notas, 1)
      return media

   def adicionar_no_cardapio(self, objeto):
      # isinstance verifica se ela derivação da classe mãe
      if isinstance(objeto, ItemCardapio):
         self._cardapio.append(objeto)

class Book:
    books = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

        Book.books.append(self)
  
    def __str__(self):
        return f'{self._titulo}\n' \
               f'       Autor: {self._autor}\n' \
               f'       Ano de Publicação: {self._ano_publicacao}\n' \
               f'       Disponibilidade: {self.disponivel}\n '
    @classmethod
    def consultor(cls):
        for book in cls.books:
            print(book)

    def emprestar_livro(self):
        self._disponivel = not self._disponivel
        return self._disponivel 
  
    @classmethod
    def verifica_disponibilidade(cls, ano):
        for book in cls.books:
          if book._disponivel == True and book._ano_publicacao == ano:
              print(book)

    @property
    def disponivel(self):
       return 'Disponivel 🔥' if self._disponivel else 'Indisponível 🥺'
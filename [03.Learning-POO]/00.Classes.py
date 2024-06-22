class Restaurante():
  def __init__(self, nome, categoria, ativo):
    self.nome = nome
    self.categoria = categoria
    self.ativo = ativo

# 1 - Atribua o valor 'Italiana' 
# ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca = Restaurante('Praça', 'italiana', True)
# print(vars(restaurante_praca))

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print('Nome: ',restaurante_praca.nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca 
# e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_praca.ativo:
  print('Restaurante está ativo')
else:
  print('Restaurante está inativo')

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
# categoria = Restaurante.categoria

# 5 - Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'
print('Nome: ',restaurante_praca.nome)

# 6 - Crie uma nova instância da classe Restaurante chamada
# restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food', False)

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
  print('A categoria é Fast Food.')
else:
  print('A categoria não é Fast Food.')

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}\nCategoria: {restaurante_praca.categoria}')
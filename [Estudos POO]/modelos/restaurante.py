class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

restaurante1 = Restaurante('Enzo', 'Pé de rato', False)
lista = [restaurante1]
print(restaurante1.nome)
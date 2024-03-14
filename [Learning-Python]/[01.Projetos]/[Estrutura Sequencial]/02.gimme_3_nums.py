# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#           i - o produto do dobro do primeiro com metade do segundo .
#           ii - a soma do triplo do primeiro com o terceiro.
#           ii - o terceiro elevado ao cubo.

while True:
  try:
    print("\tAlguns calculos:\n")

    A = int(input("Digite o primeiro valor inteiro: "))
    B = int(input("Digite o segundo valor inteiro: "))
    C = float(input("Digite o terceiro valor real: "))

    print(f"\no produto do dobro do primeiro com metade do segundo: {(A*2)*(B/2)}")
    print(f"a soma do triplo do primeiro com o terceiro: {A*3+C:.2f}")
    print(f"a soma do triplo do primeiro com o terceiro: {C**3:.2f}")

    break
  except ValueError:
    print(f"\tDigite os valores corretamente!!!")


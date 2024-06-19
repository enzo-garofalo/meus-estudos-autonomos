# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
print(f"\tTipo de triângulos!")

while True:
  try:
    t1 = float(input(f"\nDigite o primeiro lado do triângulo : "))
    t2 = float(input(f"Digite o segundo lado do triângulo  : "))
    t3 = float(input(f"Digite o terceiro lado do triângulo : "))

    if t1 <= 0 or t2 <= 0 or t3 <= 0:
      print(f"\nValores inválidos. Por favor, insira  números válido para os lados do triângulo.")
      continue

    if t1 >= t2 + t3 or t2 >= t1 + t3 or t3 >= t1 + t2:
      print(f"\nOs valores dos lados não formam um triângulo. Tente novamente!")
      continue

    if t1 == t2 == t3:
      print(f"\tO seu triângulo é equilátero!")
    elif t1 == t2 or t2 == t3 or t3 == t1:
      print(f"\tO seu triângulo é isóceles!")
    else:
      print(f"\tO seu triângulo é escaleno!")     
    break

  except ValueError:
    print(f"\tEntrada inválida. Por favor, insira um número válido para os lados do triângulo.")
    continue
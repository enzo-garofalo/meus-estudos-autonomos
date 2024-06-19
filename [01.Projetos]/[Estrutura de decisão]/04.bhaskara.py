# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
import math
print(f"\tCalculando raízes!")

def calcular_delta(a, b, c):
  return (b**2) - (4*a*c)

def calcular_raízes(a, b, c):
  delta = calcular_delta(a, b, c)
  if delta < 0:
    return None, None
  elif delta == 0:
    raiz1 = -b / (2*a)
    return raiz1
  else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    return raiz1, raiz2
  
while True:
  try:
    a = float(input("\nDigite o valor de A: "))
    if a == 0:
      print(f"\n\tValor de A não pode se igual a zero!")
      print(f"\tTente novamente!!")
      continue
    else:
      b = float(input("Digite o valor de B: "))
      c = float(input("Digite o valor de C: "))

    raiz1, raiz2, delta = calcular_raízes(a, b, c)
    print(f"\n\tEquação: {a} X² + {b} X + {c} = 0\n")

    if raiz1 is None:
      print(f"\nDelta é igual a {calcular_delta(a, b, c)}, negativo, portanto, a equação não tem raízes reais!")
    elif raiz2 is None:
      print(f"\nA raíz da equação é: {raiz1}")
    else:
      print(f"\nA primeira raíz da equação é: {raiz1:.2f}")
      print(f"A segunda raíz da equação é: {raiz2:.2f}")

    choice = input("\nDesejar calcular novamente?\n[SIM/NÃO]: ").upper()
    if choice == "SIM":
      continue
    elif choice == "NÃO" or choice == "NAO":
      print("\n\tAté mais!!!")
      break
    else:
      print("\n\tEscolha incorreta!\n\tSistema interrompido!")
      break
    
  except ValueError:
    print(f"\tEntrada inválida. Por favor, insira um número válido a equacação.")
    continue

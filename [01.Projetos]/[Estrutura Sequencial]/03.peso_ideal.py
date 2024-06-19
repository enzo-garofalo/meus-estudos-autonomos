# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print(f"\tPeso Ideal!")

def height_men(height):
    return (72.7*height/100) - 58
def height_women(height):
    return (62.1*height/100) - 44.7

while True:
  try:
    choice = input("\nQual sexo do paciente Masculino(m) ou Feminino(f): ")
    height = float(input("Digite a altura do paciente em cm: "))

    if choice == "m":
      print(f"O peso ideal para o paciente é {height_men(height):.2f}Kg")
      break
    elif choice == "f":
      print(f"O peso ideal para o paciente é {height_women(height):.2f}Kg")
      break
    else:
      print(f"Digite uma opção correta!")
  except ValueError:
    print("\nDigite os valores corretamente!\n")
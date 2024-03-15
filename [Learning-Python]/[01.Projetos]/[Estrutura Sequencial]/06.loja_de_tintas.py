# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print(f"\tLoja de tintas!")

while True:
  try:
    metros = float(input(f"\nDigite em M² a área para pintar: "))
    total_tinta = (metros / 6) * 1.10

    latas = total_tinta / 18
    galoes = (total_tinta % 18)  / 3.6

    latas = int(latas)
    galoes = int(galoes)

    print(f"\nVocê precisará de: {total_tinta:.2f} litros")
    print(f"Você usará {galoes} Galões e {latas} Latas")
    print(f"Total: R${galoes*25+(latas*80):.2f}")

    choice = input("\nDesejar calcular novamente?\n[SIM/NÃO]: ")

    if choice.upper() != "SIM":
      print("\n\tAté Mais!!")
      break
    else:
      continue

  except ValueError:
    print(f"\n\tValor digitado incorretamente!\n\tTente novamente")
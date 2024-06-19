# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20% salários entre R$ 280,00 e R$ 700,00 : aumento de 15% salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado

print(f"\tCalculadora de salários!")

while True:
  try:
    salario = float(input(f"\nDigite o salário do colaborador: "))

    if salario < 0:
      print(f"\n\tValor digitado errado, Tente novamente!")
      continue

    if salario <= 280:
      aumento = 20
    elif salario > 280 and salario < 700:
      aumento = 15
    elif salario > 700 and salario < 1500:
      aumento = 10
    else:
      aumento = 5

    print(f"\nSalário antes do reajuste: {salario:.2f}")
    print(f"Percentual de aumento aplicado: {aumento}%")
    valor_aumento = (aumento / 100) * salario
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    novo_salario = salario + valor_aumento
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")

    choice = input("\nDesejar calcular novamente?\n[SIM/NÃO]: ")
    if choice.upper() != "SIM":
      print("\n\tAté mais!!!")
      break
    else:
      continue

  except ValueError:
    print(f"\n\tValor digitado errado, Tente novamente!")
    continue
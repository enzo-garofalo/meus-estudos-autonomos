# Este programa pede para você inserir quanto ganha por hora e quantas horas trabalhou em um mês. 
# Ele então calcula seu salário bruto e os descontos, que incluem 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. 
# No final, mostra seu salário líquido."

print(f"\tCálculo de salário líquido")

while True:
  try:
    horasTrabalhadas = int(input(f"\nDigite a quantidade de horas trabalhadas: "))
    valorHoras = float(input("Digite o valor da hora de trabalho: "))
    salarioBruto = horasTrabalhadas*valorHoras
    IR = salarioBruto*0.11
    INSS = salarioBruto*0.08
    sindicato = salarioBruto*0.05
    salarioLiquido = salarioBruto-IR-INSS-sindicato

    print(f"+ Salário Bruto: R${salarioBruto:.2f}")
    print(f"- IR (11%): R${IR:.2f} ")
    print(f"- INSS (8%): R${INSS:.2f} ")
    print(f"- Sindicato (5%): R${sindicato:.2f} ")
    print(f"= Salário Líquido: R$ {salarioLiquido:.2f} ")

    choice = input("\nDesejar calcular novamente?\n[SIM/NÃO]: ")
    if choice.upper() == "SIM":
      continue
    elif choice.upper() == "NÃO" or "NAO":
      print("\n\tAté mais!!!")
      break
    else:
      print("\n\tEscolha incorreta!\n\tSistema interrompido!")
      break
  except ValueError:
    print(f"\n\tValor digitado incorretamente!\n\tTente novamente")
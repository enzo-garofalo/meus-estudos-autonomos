print(f"\tFolha de pagamentos!")

while True:
  try:
    horasTrabalhadas = int(input(f"\nDigite a quantidade de horas trabalhadas   : "))
    valorHoras = float(input("Digite o valor da hora de trabalho         : "))
    salarioBruto = horasTrabalhadas*valorHoras

    if salarioBruto <= 0:
      print("Valores digitados incorretamente, Tente novamente!")
      continue

    if salarioBruto <= 900:
      desconto = 0
    elif salarioBruto > 900 and salarioBruto < 1500:
      desconto = 5
    elif salarioBruto > 1500 and salarioBruto < 2500:
      desconto = 10
    else:
      desconto = 20
    
    IR = (desconto/100)*salarioBruto
    INSS = salarioBruto*0.10
    FGTS = salarioBruto*0.11

    print(f"\nSalário Bruto ({horasTrabalhadas} x R${valorHoras:.2f})    : {salarioBruto}")
    print(f"(-) IR ({desconto}%)                    : {IR:.2f}")
    print(f"(-) INSS (10%)                 : {INSS:.2f}")
    print(f"FGTS (11%)                     : {FGTS:.2f}")
    print(f"Total de descontos             : {IR+INSS:.2f}")
    print(f"Salário Liquido                : {salarioBruto-(IR+INSS):.2f}")
    
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
    print("Valores digitados incorretamente, Tente novamente!")
    continue
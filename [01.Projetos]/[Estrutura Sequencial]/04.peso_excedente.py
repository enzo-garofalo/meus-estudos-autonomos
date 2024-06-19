# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade 
# de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print(f"\tRendimento diário")
while True:
  try:
    peso = float(input(f"\nDigite o peso total de peixes: "))
    excesso = max(0, peso - 50) 
    multa = excesso*4
    
    print(f"Total excedente  = {excesso:.2f}KG")
    print(f"Total a ser pago = R${multa:.2f}")


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

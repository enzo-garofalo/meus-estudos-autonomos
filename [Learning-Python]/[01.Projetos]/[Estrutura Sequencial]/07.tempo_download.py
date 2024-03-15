# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print(f"\tQuanto tempo para download?")
while True:
  try:
    tamanhoArquivo = int(input(f"\nDigite o tamanho do arquivo (em MB): "))
    velocidade = float(input("Digite a velocidade da internet (em Mbps): "))

    print(f"\nTempo estimado de download: {(tamanhoArquivo/(velocidade/8))/60} minutos ou {tamanhoArquivo/(velocidade/8)} segundos")

    break
  except ValueError:
    print(f"\n\tValor digitado errado, Tente novamente!")
    continue

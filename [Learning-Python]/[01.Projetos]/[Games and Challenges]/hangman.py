import random

# Função para escolher uma palavra aleatória da lista de palavras secretas
def def_palavras_secretas():
    palavras_secretas =  [
    "lionel messi", "cristiano ronaldo", "neymar", "kylian mbappe", "robert lewandowski",
    "kevin de bruyne", "sergio ramos", "virgil van dijk", "mohamed salah", "sadio mane", "vinicius junior"
    "harry kane", "antoine griezmann", "luka modric", "sergio aguero", "luis suarez",
    "karim benzema", "eden hazard", "paul pogba","pele", "diego maradona", "johan cruyff", 
    "beckenbauer", "michel platini","di stefano", "zlatan ibrahimovic", "puskas",
    "xavi", "iniesta","ronaldo", "garrincha", "paolo maldini", "zinedine zidane", "renato augusto"
    "paçoca", "banana", "cachaça", "capitalismo", "python", "picole", "abobora", "coelho", "sauna", 
    "oculos", "fisiculturismo"
    ]
    palavra = random.choice(palavras_secretas)  # Escolha aleatória da palavra
    palavra = list(palavra)  # Converte a palavra em uma lista de caracteres
    return palavra

# Função para perguntar ao jogador se deseja jogar novamente
def jogar_novamente():
    choice = input("\nDeseja jogar novamente?\n[SIM/NÃO]: ").upper()  # Entrada do jogador em maiúsculas

    # Verifica a escolha do jogador e decide se deve jogar novamente ou sair
    if choice == "SIM":
        forca()  # Chama a função principal para começar um novo jogo
    elif choice == "NÃO" or choice == "NAO":
        print(f"\n\tObrigado por jogar!!!")  # Mensagem de despedida
    else:
        print(f"\n\tEscolha incorreta!\n\tSistema interrompido!")  # Mensagem de erro para escolha inválida

# Função principal para executar o jogo da forca
def forca():
    tentativas = 6  # Número de tentativas permitidas
    digitadas = []  # Lista para armazenar letras já digitadas

    palavra_secreta = def_palavras_secretas() # Chama a função para escolher uma palavra secreta aleatória
    palavra_print = ["-" if letra != " " else " " for letra in palavra_secreta]  # Lista para armazenar letras reveladas e traços

    # Loop principal do jogo
    while tentativas > 0 and "-" in palavra_print:
        try:
            print(f"\nPalavra secreta: ", "".join(palavra_print).upper())  # Exibe a palavra parcialmente revelada

            letra = str(input("Digite uma letra: "))  # Solicita uma letra ao jogador

            # Verifica se a entrada do jogador é uma única letra
            if  len(letra) != 1:
                print(f"\nDigite uma letra por vez! Tente novamente!")
                continue
            elif letra in digitadas:
                print(f"\nEssa letra já foi!! Tente novamente!")
                continue
            else:
                digitadas.append(letra)  # Adiciona a letra à lista de letras digitadas

                # Verifica se a letra está presente na palavra secreta
                if letra in palavra_secreta:
                    for i in range(len(palavra_secreta)):
                        if letra == palavra_secreta[i]:
                            palavra_print[i] = letra  # Atualiza a lista de letras reveladas
                    print(f"Letra correta!\n")
                else:
                    tentativas -= 1  # Decrementa o número de tentativas restantes
                    print(f"Letra incorreta!, Você tem {tentativas} Chances.\n")

        except ValueError:
            print(f"Valor digitado incorreto, tente novamente!\n")
            continue

    # Verifica se o jogador ganhou ou perdeu
    if "-" not in palavra_print:
        print(f"\n\tParabéns! Você acertou a palavra secreta:", "".join(palavra_secreta).upper())
        jogar_novamente()  # Pergunta ao jogador se deseja jogar novamente
    else:
        print("Você perdeu! A palavra secreta era:", "".join(palavra_secreta).upper())
        jogar_novamente()  # Pergunta ao jogador se deseja jogar novamente

# Início do jogo
print(f"\tHangman!")
forca()  # Chama a função principal para iniciar o jogo
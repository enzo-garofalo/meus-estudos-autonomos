import os
from prettytable import PrettyTable
# Definição da função para cadastrar um novo produto
def cadastrar_produto():
    os.system("cls")  # Limpa a tela do console (apenas Windows)

    print(f"\n\tCadastro de produto!")  # Mensagem de cabeçalho para o cadastro
    # Solicita e armazena os dados do produto inseridos pelo usuário
    global cod_prod
    cod_prod = int(input("Código do produto: "))
  
    global nome_prod
    nome_prod = input("Nome do produto: ")
    
    global desc_prod
    desc_prod = input("Descrição: ")
    
    global custo_prod
    custo_prod = float(input("Custo de compra: R$ "))
    
    global custo_fixo_prod
    custo_fixo_prod = float(input("Custo fixo/administrativo [%]: "))

    global comissao_vendas
    comissao_vendas = float(input("Comissão de vendas [%]: "))

    global imposto_prod
    imposto_prod = float(input("Imposto sobre a venda [%]: "))

    global lucro_prod
    lucro_prod = float(input("Margem de lucro [%]: "))

    os.system("cls")
    print(tabela())
    avancar()

def tabela():
    global table
    table = PrettyTable()
    table.add_column(f"Código do Produto",[cod_prod])
    table.add_column(f"Nome",[nome_prod])
    table.add_column(f"Descrição",[desc_prod])
    table.add_column(f"Custo de Compra",[custo_prod])
    table.add_column(f"Custo Fixo/Administrativo",[custo_fixo_prod])
    table.add_column(f"Comissão de vendas",[comissao_vendas])
    table.add_column(f"Imposto sobre a venda",[imposto_prod])
    table.add_column(f"Margem de lucro",[lucro_prod])
    return table

# Definição da função para calcular o preço de venda, custos e rentabilidade do produto
def calculo_preco():
    # Cálculo do preço de venda
    preco_venda = (custo_prod) / (1 - ((custo_fixo_prod + comissao_vendas + imposto_prod + lucro_prod) / 100))
    # Cálculo dos custos
    custos = preco_venda * ((custo_fixo_prod + comissao_vendas + imposto_prod) / 100)
    # Cálculo da rentabilidade
    rentabilidade = ((preco_venda / custo_prod) - 1) * 100
    # Exibição dos resultados
    print(f"O preço de venda do produto é R${preco_venda:.2f}, o lucro bruto é {rentabilidade:.2f}% e os custos são de {custos:.2f}")
    # Verifica a rentabilidade e exibe uma mensagem correspondente
    if rentabilidade >= 20:
        print("\nO lucro foi alto")
    elif 20 > rentabilidade >= 10:
        print("\nO lucro foi médio")
    elif 10 > rentabilidade >= 0:
        print("\nO lucro foi baixo")
    else:
        print("\nFicou no prejuízo")
    # Retorna o preço de venda, custos e rentabilidade
    return preco_venda, custos, rentabilidade

def avancar():
    os.system("cls")

    choice = input(f"\nDeseja mudar algo?\n[SIM/NÃO]: ").upper()  # Entrada do jogador em maiúsculas

    # Verifica a escolha do jogador e decide se deve jogar novamente ou sair
    if choice == "SIM":
        escolha = int(input(f"\t O que deseja alterar?\n\t| 1- Código do produto     |\n\t| 2- Nome                  |\n\t| 3- Descrição             |\n\t| 4- Custo de compra       |\n\t| 5- Comissão de venda     |\n\t| 6- Imposto sobre a venda |\n\t| 7- Margem de lucro       |\n\n\tDigite uma opção: "))  # Chama a função principal para começar um novo jogo
        match escolha:
        # Caso a escolha seja 1 (Cadastrar)
          case 1:
              cod_prod = int(input("Digite o novo código do produto: ")) # Chama a função para cadastrar um produto
              print(tabela())
              avancar()
              
        # Caso a escolha seja 2 (Listar)
          case 2:
              listagem_de_dados()  # Chama a função para listar dados (não definida no código fornecido)
        # Caso a escolha seja 3 (Alterar)
          case 3:
              alteracao_de_dados()  # Chama a função para alterar dados (não definida no código fornecido)
        # Caso a escolha seja 4 (Excluir)
          case 4:
              exclusao_de_dados()  # Chama a função para excluir dados (não definida no código fornecido)
        # Caso a escolha seja 5 (Sair)
          case 5:
              print(f"Até mais!")  # Exibe mensagem de despedida
              exit()  # Encerra o programa
        # Caso a escolha não seja válida
          case default:
              print("Digite uma opção válida")  # Exibe uma mensagem indicando uma escolha inválida

    elif choice == "NÃO" or choice == "NAO":
        calculo_preco()  # Mensagem de despedida
    else:
        print(f"\n\tEscolha incorreta!\n\tSistema interrompido!")
        exit()  # Mensagem de erro para escolha inválida



# Função principal
def main():
    # Exibe o menu e solicita a escolha do usuário
    escolha = int(input(f"\t     MENU\n\t| 1- Cadastrar |\n\t| 2- Listar    |\n\t| 3- Alterar   |\n\t| 4- Excluir   |\n\t| 5- Sair      |\nO que deseja fazer? "))
    # Verifica a escolha do usuário
    match escolha:
        # Caso a escolha seja 1 (Cadastrar)
        case 1:
            cadastrar_produto()  # Chama a função para cadastrar um produto
        # Caso a escolha seja 2 (Listar)
        case 2:
            listagem_de_dados()  # Chama a função para listar dados (não definida no código fornecido)
        # Caso a escolha seja 3 (Alterar)
        case 3:
            alteracao_de_dados()  # Chama a função para alterar dados (não definida no código fornecido)
        # Caso a escolha seja 4 (Excluir)
        case 4:
            exclusao_de_dados()  # Chama a função para excluir dados (não definida no código fornecido)
        # Caso a escolha seja 5 (Sair)
        case 5:
            print(f"Até mais!")  # Exibe mensagem de despedida
            exit()  # Encerra o programa
        # Caso a escolha não seja válida
        case default:
            print("Digite uma opção válida")  # Exibe uma mensagem indicando uma escolha inválida
            main()  # Chama novamente a função principal para que o usuário faça uma nova escolha

# Chamada da função principal
main()

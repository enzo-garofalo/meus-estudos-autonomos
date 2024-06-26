import requests
import json
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Get, verbo https solicitador de recursos, dados
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)

# from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
# from modelos.cardapio.prato import Prato

# restaurante_1 = Restaurante('Seu Mário', 'Gourmet', 300)
# restaurante_2 = Restaurante('Seu Joaquim', 'Italiano', 300)
# restaurante_3 = Restaurante('Temakeria.Com', 'Ruim', 300)

# bebida = Bebida('Suco de melancia', 5.00, 'Grande')
# prato  = Prato('Strogonoff', 2.00, 'Strogonoff de filé mignon')

# bebida.aplicar_desconto()
# prato.aplicar_desconto()

# restaurante_1.adicionar_no_cardapio(bebida)
# restaurante_1.adicionar_no_cardapio(prato)

# def main():
#     restaurante_1.consultar_cardapio

# if __name__ == '__main__':
#     main()
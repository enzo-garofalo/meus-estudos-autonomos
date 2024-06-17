# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = 0

for pergunta in perguntas:
    resposta = 0
    
    print('-'*30+'\n'+pergunta)

    resposta = int(input('[1-Sim | 2-Não]: '))
    if resposta == 1:
        respostas += 1 

if respostas in [3,4]:
    respostas = 3
    
vereditos = {'Suspeito': 2, 'Cumplice':3, 'Assasino': 5, 'Inocente': 0}
for veredito, valores in vereditos.items():
    if respostas == valores:
        print(veredito)
    
    



# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re
S = "jjhv"
K = "z"

# Cria o padrão para fazer busca na STRING - S, O ? não retira o K dos indices.
padrao_busca = re.compile(f'(?=({K}))')
# Cria uma tupla com cada indice encontrado em S
check = list(padrao_busca.finditer(S))

# Para cada padrão encontrado vai imprimir os indices aonde as letras desse indice foi encontrado
for substring in check:
  print(substring.start(1), substring.end(1)-1)

if not check:
  print("(-1, -1)")
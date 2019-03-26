"""
# Execicio 1

from random import randrange

matriz = [[randrange(0, 50) for numero in range(4)] for valor in range(4)]
contador = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if matriz[linha][coluna] > 10:
            contador += 1
print(matriz)
print(f'Existem {contador} números maiores que 10')

# Exercicio 2

matriz = [['*' for coluna in range(5)] for linha in range(5)]
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if linha == coluna:
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0
print(matriz)

# Exercicio 3

matriz = [['*' for coluna in range(4)] for linha in range(4)]
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        matriz[linha][coluna] = linha * coluna
print(matriz)

# Exercicio 4
from random import randrange

matriz = [[randrange(0, 50) for numero in range(4)] for valor in range(4)]
maior = 0
localizacao = list()
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            localizacao.clear()
            localizacao.append((linha, coluna))
print(matriz)
print(localizacao)
"""

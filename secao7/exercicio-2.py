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

# Exercicio 5
from random import randrange
matriz = [[randrange(0, 50) for coluna in range(5)] for linha in range(5)]
entrada = randrange(0, 50)
x = -1
y = -1

for linha in range(5):
    for coluna in range(5):
        print(matriz[linha][coluna], end=' ')
    print()

print(f'Valor da entrada: {entrada}')

for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == entrada:
            x = linha
            y = coluna

if x == -1:
    print('Não encontrado.')
else:
    print(f'Valor encontrado na linha {x} e coluna {y}')

# Exercicio 6
from random import randrange

matriz1 = [[randrange(0, 100) for coluna in range(4)] for linha in range(4)]
matriz2 = [[randrange(0, 100) for coluna in range(4)] for linha in range(4)]

print(matriz1)
print(matriz2)

matriz_maior = [[max(matriz1[linha][coluna], matriz2[linha][coluna])
                 for coluna in range(4)] for linha in range(4)]
print(matriz_maior)

# Exercicio 7
matriz = [['*' for coluna in range(10)] for linha in range(10)]

for linha in range(10):
    for coluna in range(10):
        if linha < coluna:
            matriz[linha][coluna] = (2 * linha) + (7 * coluna) - 2
        elif linha == coluna:
            matriz[linha][coluna] = (3 * linha ** 2) - 1
        else:
            matriz[linha][coluna] = (4 * linha ** 3) - (5 * coluna ** 2) + 1
print(matriz)

# Exercicio 8
from random import randrange

matriz = [[randrange(0, 100) for coluna in range(3)] for linha in range(3)]

soma = 0
for linha in range(3):
    for coluna in range(3):
        if coluna > linha:
            soma += matriz[linha][coluna]
print(f'A soma dos valores acima da diagonal principal é {soma}')

# Exercicio 9

from random import randint

matriz = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]
soma = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if linha > coluna:
            soma += matriz[linha][coluna]

print(f'A soma dos elementos abaixo da diagonal principal é {soma}')

# Exercicio 11

from random import randint

matriz = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]
soma = 0

for linha in range(3):
    for coluna in range(3):
        if linha + coluna == len(matriz) - 1:
            soma += matriz[linha][coluna]

print(f'A soma da diagnal secundária é {soma}')

# Exercicio 12
from random import randint

matriz = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]

transposta = []
for linha in range(3):
    transposta.append([matriz[coluna][linha] for coluna in range(3)])
print()

print(f'Matriz: {matriz}\nTranposta: {transposta}')

# Exercicio 13
from random import randint
import numpy as np

ordem = 4
matriz = [[randint(1, 20) for coluna in range(ordem)] for linha in range(ordem)]

print(np.matrix(matriz))

print()
for linha in range(ordem):
    for coluna in range(ordem):
        if linha < coluna:
            matriz[linha][coluna] = 0

print(np.matrix(matriz))
"""

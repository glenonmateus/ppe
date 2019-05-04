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

# exercicio 14
from random import randint
import numpy as np

ordem = 5
cartela = [[-1 for coluna in range(ordem)] for linha in range(ordem)]


def in_matrix(numero, matriz):
    #verifica se um número está na matriz
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            if numero == matriz[i][j]:
                return true
    return false


for linha in range(ordem):
    for coluna in range(ordem):
        while true:
            numero = randint(0, 99)
            if not in_matrix(numero, cartela):
                cartela[linha][coluna] = numero
                break

print(np.matrix(cartela))

# exercicio 15
from random import choice
import numpy as np

opcoes = ['a', 'b', 'c', 'd']
garabarito = [choice(opcoes) for quantidade in range(10)]
provas = [[choice(opcoes) for resposta in range(10)] for aluno in range(5)]
resultado = []

print(f'garabarito: {garabarito}')
print(f'prova: {np.matrix(provas)}')

soma = 0
for aluno in range(5):
    for resposta in range(10):
        if provas[aluno][resposta] == garabarito[resposta]:
            soma += 1
    resultado.append(soma)
    soma = 0

print(f'resultado: {resultado}')

# Exercicio 16
from random import choice
import numpy as np

opcoes = ['a', 'b', 'c', 'd', 'e']
gabarito = [choice(opcoes) for aluno in range(10)]
print(gabarito)

provas = [[choice(opcoes) for resposta in range(10)] for aluno in range(3)]
print(np.matrix(provas))

resultado = []
soma = 0
for aluno in range(3):
    for resposta in range(10):
        if provas[aluno][resposta] == gabarito[resposta]:
            soma += 1
    resultado.append(soma)
    soma = 0

print(resultado)

# Exericio 17
from random import randint
import numpy as np

notas = [[randint(0, 10) for nota in range(3)] for aluno in range(10)]
print(np.matrix(notas))

pior_nota1 = 0
pior_nota2 = 0
pior_nota3 = 0
for aluno in range(len(notas)):
    if min(notas[aluno]) == notas[aluno][0]:
        pior_nota1 += 1
    elif min(notas[aluno]) == notas[aluno][1]:
        pior_nota2 += 1
    elif min(notas[aluno]) == notas[aluno][2]:
        pior_nota3 += 1

print(f'{pior_nota1} tiveram a pior nota na primeira prova.')
print(f'{pior_nota2} tiveram a pior nota na segunda prova.')
print(f'{pior_nota3} tiveram a pior nota na terceira prova.')

# Exercicio 18
from random import randint
import numpy as np

ORDEM = 3
matriz = [[randint(0, 50) for coluna in range(ORDEM)]
          for linha in range(ORDEM)]

print(np.matrix(matriz))

soma = 0
resultado = []
for coluna in range(ORDEM):
    for linha in range(ORDEM):
        soma += matriz[linha][coluna]
    resultado.append(soma)
    soma = 0

print(f'O resultado da soma das coluna é {resultado}')

# Exercicio 19
import numpy as np
from random import randint

matriz = [['*' for coluna in range(4)] for linha in range(5)]

maior_nota = 0
soma = 0
for linha in range(len(matriz)):
    matriz[linha][0] = randint(1, 100)
    matriz[linha][1] = randint(0, 10)
    matriz[linha][2] = randint(0, 10)
    matriz[linha][3] = matriz[linha][1] + matriz[linha][2]
    soma += matriz[linha][3]
    if matriz[linha][3] > maior_nota:
        maior_nota = matriz[linha][3]

print(np.matrix(matriz))
print(f'A maior nota final é {maior_nota}')
print(f'A média das notas finais é {soma / len(matriz)}')

# Exercicio 20
from random import randint
import numpy as np

matriz = [[randint(0, 50) for coluna in range(6)] for linha in range(3)]
print(np.matrix(matriz))

soma = 0
for linha in range(3):
    for coluna in range(1, 6, 2):
        soma += matriz[linha][coluna]

print(f'A soma dos elementos das colunas ímpares são {soma}')

soma = 0
contador = 0
for linha in range(3):
    soma += matriz[linha][1] + matriz[linha][3]
    contador += 2
media = soma / contador
print(f'A média dos elementos da segunda e quarta coluna é {media}')

soma = 0
for linha in range(3):
    matriz[linha][5] = matriz[linha][0] + matriz[linha][1]

print(np.matrix(matriz))

# Exercicio 21
from random import randint
import numpy as np

matriz1 = [[randint(0, 50) for coluna in range(2)] for linha in range(2)]
matriz2 = [[randint(0, 50) for coluna in range(2)] for linha in range(2)]
matriz_soma = []
matriz_subtracao = []

while True:
    print('''
    (a) somar as duas matrizes
    (b) subtrair a primeira matriz da segunda
    (c) adicionar uma costante às duas matrizes
    (d) imprimir as matrizes
    ''')
    opcao = input('Escolha uma das opções acima: ')
    if opcao == 'a':
        matriz_soma.clear()
        for i in range(2):
            linha = []
            for j in range(2):
                linha.append(matriz1[i][j] + matriz2[i][j])
            matriz_soma.append(linha)
    elif opcao == 'b':
        matriz_subtracao.clear()
        for i in range(2):
            linha = []
            for j in range(2):
                linha.append(matriz1[i][j] - matriz2[i][j])
            matriz_subtracao.append(linha)
    elif opcao == 'c':
        constante = int(input('Digite o valor da constante: '))
        for i in range(2):
            for j in range(2):
                matriz1[i][j] += constante
                matriz2[i][j] += constante
    elif opcao == 'd':
        print('\nMatriz 1:')
        print(np.matrix(matriz1))
        print('\nMatriz 2:')
        print(np.matrix(matriz2))
        if matriz_soma:
            print('\nMatriz Soma:')
            print(np.matrix(matriz_soma))
        if matriz_subtracao:
            print('\nMatriz Subtração:')
            print(np.matrix(matriz_subtracao))
    else:
        break

# Exercicio 22

from random import randint
import numpy as np

matriz_a = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]
matriz_b = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]
print(np.matrix(matriz_a))
print(np.matrix(matriz_b))

matriz_c = [[matriz_a[linha][coluna] * matriz_b[linha][coluna]
             for coluna in range(3)] for linha in range(3)]
print(np.matrix(matriz_c))

# Exercicio 23
from random import randint
import numpy as np

matriz_a = [[randint(0, 50) for coluna in range(3)] for linha in range(3)]
matriz_b = [[matriz_a[linha][coluna] ** 2 for coluna in range(3)]
             for linha in range(3)]
print(np.matrix(matriz_a))
print(np.matrix(matriz_b))
"""

# Exercicio 25
import numpy as np
from random import choice

opcoes = [-1, 0, 1]
tabuleiro = [[choice(opcoes) for coluna in range(3)] for linha in range(3)]
print(np.matrix(tabuleiro))

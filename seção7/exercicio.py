"""
# Exercicio 1
A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(A)
print(f'A soma dos valores {soma}')
A[3] = 100
for i in A:
    print(i)

# Exercicio 2
lista = []
for i in range(6):
    entrada = int(input('Digite um número: '))
    lista.append(entrada)
print(lista)

# Exercicio 3
lista = []
lista_quadrado = []
for i in range(10):
    entrada = int(input('Digite um número: '))
    lista.append(entrada)
for i in lista:
    lista_quadrado.append(i ** 2)
print(lista)
print(lista_quadrado)

# Exercicio 4
lista = []
for i in range(8):
    entrada = float(input('Digite um número: '))
    lista.append(entrada)
posicao1 = int(input('Digite a primeira posição da lista: '))
if posicao1 > 8 or posicao1 < 0:
    print('Posição inválida.')
    quit()
posicao2 = int(input('Digite a segunda posição da lista: '))
if posicao2 > 8 or posicao2 < 0:
    print('Posição inválida.')
    quit()
soma = lista[posicao1] + lista[posicao2]
print(f'A soma dos valores das posições escolhidas é {soma}')

# Exercicio 8
lista = []
for i in range(6):
    entrada = int(input('Digite um valor inteiro: '))
    lista.append(entrada)
print(lista[::-1])
lista.reverse()
print(lista)

# Exercicio 10
from random import randrange
notas = []
for i in range(15):
    nota = randrange(10)
    print(f'a nota do aluno {i} é {nota}')
    notas.append(nota)
print(f'A média geral das notas {sum(notas) / 15}')

# Exercicio 21
from random import randrange
listaA = []
listaB = []
listaC = []
for i in range(10):
    listaA.append(randrange(100))
    listaB.append(randrange(100))
    listaC.append(listaA[i] - listaB[i])
print(listaA)
print(listaB)
print(listaC)

# Exercicio 20
from random import randrange
lista1 = []
lista2 = []
for i in range(10):
    lista1.append(randrange(0, 50))
    if lista1[i] % 2 != 0:
        lista2.append(lista1[i])
for i in range(len(lista1)):
    print(lista1[i], end=' ')
    if lista1.index(lista1[i]) % 2 != 0:
        print()
print()
for i in range(len(lista2)):
    print(lista2[i], end=' ')
    if lista2.index(lista2[i]) % 2 != 0:
        print()

# Exercicio 26
from random import randrange
from math import sqrt

lista = []
for i in range(10):
    lista.append(randrange(0, 50))
print(lista)

media = sum(lista) / len(lista)
print(f'A média da amostra de dados é {media}')

somatorio = 0
for i in range(len(lista)):
    somatorio += (lista[i] - media) ** 2
print(f'O somatório é {somatorio}')

desvio_padrao = sqrt(somatorio / len(lista))
print(f'O desvio padrão do conjunto de dados é {desvio_padrao}')
"""



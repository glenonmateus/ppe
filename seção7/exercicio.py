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

# Exercicio 27
from random import randrange
lista = []
for i in range(10):
    lista.append(randrange(0, 50))
print(lista)

primo = True
for i in range(len(lista)):
    for j in range(2, lista[i]):
        if lista[i] % j == 0:
            primo = False
            break
    if primo:
        print(f'O elemento {lista[i]} é primo e está na posição {i}')
    else:
        print(f'O elemento {lista[i]} não é primo e está na posição {i}!')
    primo = True

# Exercicio 28
from random import randrange
v = []
v1 = []
v2 = []
for i in range(10):
    v.append(randrange(0, 50))
print(v)

for i in range(len(v)):
    if v[i] % 2 == 0:
        v1.append(v[i])
    else:
        v2.append(v[i])
print(f'Os valores pares do vetor v é \n{v1}')
print(f'Os valores ímpares do vetor v é \n{v2}')

# Exercicio 30
from random import randrange
conjunto1 = set()
conjunto2 = set()

for i in range(10):
    conjunto1.add(randrange(0, 50))
    conjunto2.add(randrange(0, 50))
print(conjunto1)
print(conjunto2)
print(conjunto1.intersection(conjunto2))

# Exercicio 31
from random import randrange
v1 = set()
v2 = set()
for i in range(10):
    v1.add(randrange(0, 50))
    v2.add(randrange(0, 50))
print(v1)
print(v2)
print(v1.union(v2))

# Exercicio 32
from random import randrange
x = []
y = []
for i in range(5):
    x.append(randrange(0, 50))
    y.append(randrange(0, 50))
print(f'x: {x}')
print(f'y: {y}')

print('Soma: ', end='')
for i in range(len(x)):
    print(x[i] + y[i], end=' ')

print('\nMultiplicação: ', end='')
for i in range(len(x)):
    print(x[i] * y[i], end=' ')

conjunto_x = set(x)
conjunto_y = set(y)
print(f'\nDiferença: {conjunto_x.difference(conjunto_y)}')
print(f'Interseção: {conjunto_x.intersection(conjunto_y)}')
print(f'União: {conjunto_x.union(conjunto_y)}')
"""


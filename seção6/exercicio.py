"""
# Exercicio 2
print('1 a 100 com for')
for i in range(1, 101):
    print(i)

print('1 a 100 com while')
i = 1
while i < 101:
    print(i)
    i += 1

# Exercicio 3
import time
contagem = 10
while contagem >= 0:
    print(f'Contagem regressiva {contagem}')
    time.sleep(1)
    contagem -= 1
print('FIM!')

# Exercicio 21

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = 0
mult = 1

for i in range(num1, num2+1):
    if i % 2 == 0:
        soma += i
    else:
        mult *= i

print(f'A soma dos valores pares: {soma}')
print(f'A multiplicação dos valores ímpares: {mult}')

# Exercicio 22

nota = 0
soma = 0
contador = 0

while True:
    nota = float(input('Digite a nota: '))
    if 10 <= nota <= 20:
        soma += nota
        contador += 1
    else:
        break

media = soma / contador
print(f'A média dos valores: {media}')

# Exercicio 23

num = int(input('Digite um número: '))
for valor in range(1, num+1):
    if num % valor == 0:
        print(valor)

# Exercicio 24

soma = 0
num = int(input('Digite um número: '))
for valor in range(1, num):
    if num % valor == 0:
        soma += valor
print(f'A soma dos dividores do {num} é {soma}')

# Exercicio 25

soma = 0
for valor in range(1, 1001):
    if valor % 3 == 0 or valor % 5 == 0:
        soma += valor
print(soma)

# Exercicio 26

num = int(input('Digite um número: '))
while True:
    num += 1
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        print(num)
        break

# Exercicio 27

num = int(input('Digite um número: '))
harmonico = 1
for i in range(2, num+1):
    harmonico += 1 / i
print(f'Número harmônico de {num} é {harmonico}')

# Exercicio 28

from math import factorial
num = int(input('Digite um número: '))
e = 1
for i in range(1, num + 1):
    e += 1 / factorial(i)
print(f"O valor 'e' é {e}")

# Exercicio 29

from math import factorial
serie = 0
for i in range(1, 6):
    serie += i / factorial(i * 2)
print(f'O valor da série é {serie}')

# Exercicio 31

soma = 1
divisor = 1
for i in range(3, 100, 2):
    divisor += 1
    soma += i / divisor
print(soma)

# Exercicio 32
from random import randrange
n = int(input('Digite quantas vezes os dados serão lançados: '))
for i in range(n):
    dado1 = randrange(1, 6)
    dado2 = randrange(1, 6)
    if dado1 > dado2:
        print(f'O dado 1 ({dado1}) é maior que o dado 2 ({dado2}).')
    elif dado1 < dado2:
        print(f'O dado 2 ({dado2}) é maior que o dado 1 ({dado1}).')
    else:
        print(f'Os dados tem o mesmo valor (dado1 ({dado1}) = dado2 ({dado2})).')

# Exercicio 35
soma = 0
inicial = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
if inicial > final:
    print('Intervalo de valores inválido.')
    quit()
for i in range(inicial, final+1):
    if i % 2 == 1:
        print(f'Somando o valor {i} ...')
        soma += i
print(f'A soma dos ímpares é {soma}')
"""

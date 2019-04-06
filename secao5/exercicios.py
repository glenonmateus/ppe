"""
Lista de exercicios

# Exercicio 1

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é {numero1}')
elif numero2 > numero1:
    print(f'O maior número é {numero2}')
else:
    print(f'Os números são iguais')

# Exercicio 2

numero = float(input('Digite um número: '))

if numero > 0:
    raiz = numero ** (1/2)
    print(raiz)
else:
    print('Número inválido')

# Exercicio 3

numero = float(input('Digite um número: '))

if numero > 0:
    print(numero ** (1/2))
else:
    print(numero ** 2)

# Exercicio 5

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Número par')
else:
    print('Número ímpar')

# Exercicio 8

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10):
    print(f'A média é {(nota1+nota2)/2}')
else:
    print('Nota inválida.')

# Exercicio 9

salario = float(input('Digite o salário: '))
prestacao = float(input('Digite o valor da prestação: '))

if prestacao <= salario * 0.2:
    print('Empréstimo concedido.')
else:
    print('Empréstimo não concedido.')

# Exercicio 10
altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo: ')

if sexo == 'masculino':
    print(f'Peso ideal: {(72.7 * altura) - 58}')
elif sexo == 'feminino':
    print(f'Peso ideal: {(62.1 * altura) - 44.7}')

# Exercicio 11
inteiro = input('Digite um número inteiro: ')
if int(inteiro) > 0:
    soma = 0
    for num in inteiro:
        soma += int(num)
    print(soma)
else:
    print('Número inválido.')

# Exercicio 12
import math
inteiro = int(input('Digite um número inteiro: '))
if inteiro < 0:
    print('Número inválido.')
else:
    print(math.log2(inteiro))

# Exercicio 13
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota3 = nota3 * 2
media = (nota1 + nota2 + nota3) / 4
print(f'A média é {media}')
if media < 60:
    print('Reprovado.')
else:
    print('Aprovado.')

# Exercicio 14
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota1 = nota1 * 2
nota2 = nota2 * 3
nota3 = nota3 * 5
media = (nota1 + nota2 + nota3) / 10
print(f'A média é {media}')
if media < 2.9:
    print('Reprovado.')
elif media < 4.9:
    print('Recuperação.')
else:
    print('Aprovado.')

# Exercicio 18
opcao = int(input(""Digite a operação que quer fazer:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
""))

if opcao < 0 or opcao > 4:
    print('Opção Inválida')
else:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo núemro: '))

if opcao == 1:
    print(num1 + num2)
elif opcao == 2:
    print(num1 - num2)
elif opcao == 3:
    print(num1 * num2)
elif opcao == 4:
    print(num1 / num2)

# Exercicio 19
inteiro = int(input('Digite um número inteiro: '))
if inteiro % 3 == 0 and inteiro % 5 == 0:
    print(f'O {inteiro} é divisível por 3 e por 5')
elif inteiro % 3 == 0:
    print(f'O {inteiro} é divisível por 3')
elif inteiro % 5 == 0:
    print(f'O {inteiro} é divisível por 5')

# Exercicio 23
ano = int(input('Digite um ano: '))
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('Ano bissexto')
else:
    print('Ano não bissexto')

# Exercicio 24
valor = float(input('Digite o valor do produto: '))
destino = input('Digite o estado destino do produto: ').upper()
if destino == 'MG':
    print(f'Valor final {valor + valor * 0.07}')
elif destino == 'SP':
    print(f'Valor final do produto {valor + valor * 0.12}')
elif destino == 'RJ':
    print(f'Valor final do produto {valor + valor + 0.15}')
elif destino == 'MS':
    print(f'Valor final do produto {valor + valor + 0.08}')
else:
    print('Destino inválido.')

# Exercicio 26
km = float(input('Digite a distancia: '))
litros = float(input('Digite a quantidade de litros consumida: '))
consumo = km / litros
if consumo < 8:
    print('Venda o carro!')
elif consumo >= 8 and consumo <= 14:
    print('Econômico!')
elif consumo > 14:
    print('Super econômico!')

# Exercicio 27
idade = int(input('Digite a idade: '))
if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade > 7 and idade <= 10:
    print('Infantil B')
elif idade > 10 and idade <= 13:
    print('Juvenil A')
elif idade > 13 and idade <= 17:
    print('Juvenil B')
elif idade > 17:
    print('Maiores de 18 anos')

# Exercicio 29
import random
acertos = 0
for chance in range(5):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f'Qual a soma de {num1} + {num2}')
    resposta = int(input('Digite a resposta: '))
    if resposta == num1 + num2:
        print('Resposta correta')
        acertos += 1
    else:
        print('Resposta incorreta')
print(f'Você acertou {acertos} vezes')

# Exercicio 30
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
lista = [num1, num2, num3]
lista.sort()
print(lista)

# Exercicio 31
altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
if altura < 1.20:
    if peso <= 60:
        print('A')
    elif peso > 60 and peso <= 90:
        print('D')
    elif peso > 90:
        print('G')
elif altura > 1.20 and altura <= 1.70:
    if peso <= 60:
        print('B')
    elif peso > 60 and peso <= 90:
        print('E')
    elif peso > 90:
        print('H')
elif altura > 1.70:
    if peso <= 60:
        print('C')
    elif peso > 60 and peso <= 90:
        print('F')
    elif peso > 90:
        print('I')

# Exercicio 33
preco = float(input('Digite o preço do produto: '))
if preco < 50:
    preco += preco * 0.05
elif preco >= 50 and preco < 100:
    preco += preco * 0.1
elif preco > 100:
    preco += preco * 0.15
print(f'O preço novo do produto {preco}')

# Exercicio 40
custo_fabrica = float(input('Digite o custo de fábrica: '))
if custo_fabrica <= 12000:
    print(f'O custo ao consumidor é {custo_fabrica + custo_fabrica * 0.05}')
elif custo_fabrica > 12000 and custo_fabrica <= 25000:
    print(f'O custo ao consumidor é {custo_fabrica + custo_fabrica * 0.1 + custo_fabrica * 0.15}')
elif custo_fabrica > 25000:
    print(f'O custo ao consumidor é {custo_fabrica + custo_fabrica * 0.15 + custo_fabrica * 0.2}')
else:
    print('Valor inválido.')

 # Exercicio 41
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)
print(f'IMC = {imc}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.6 < imc < 25:
    print('Saudável')
elif 25 <= imc < 30:
    print('Peso em excesso')
elif 30 <= imc < 35:
    print('Obesidade Grau I')
elif 35 <= imc < 40:
    print('Obesidade Grau II (severa)')
elif 40 <= imc:
    print('Obesidade Grau III (mórbida)')
"""
# Exercicio 37
hora_entrada = int(input('Digite a hora da entrada: '))
minuto_entrada = int(input('Digite o minuto da entrada: '))
hora_saida = int(input('Digite a hora da saída: '))
minuto_saida = int(input('Digite o minuto da saída: '))
print(f'Hora da entrada: {hora_entrada} {minuto_entrada}')
print(f'Hora da saída: {hora_saida} {minuto_saida}')

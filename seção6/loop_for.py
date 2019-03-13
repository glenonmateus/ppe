"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

# Python

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
    String -> nome = 'Geek University'
    Lista -> [1, 2, 3, 4]
    Range -> numeros = range(1, 10)

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for item in lista:
    print(item)

# Exemplo de for 3 (iterando sobre uma range)
for numero in range(1, 10):
    print(numero)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.

Enumerate:
    ((0,'G'), (1,'e'), (2,'e'), (3,'k') ...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

quantidade = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, quantidade+1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma += num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Original: U+1F60D
# Modificado: U0001F60D

emoji = '\U0001F60D'

for _ in range(2):
    for num in range(1, 11):
        print(f'{emoji * num}')

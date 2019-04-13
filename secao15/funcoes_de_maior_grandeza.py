"""
Funções de maior grandeza - higher order functions - HOF

O que isso significa?
    - quando uma linguagem de programação suporta HOF, indica que podemos ter
    funções que retornam outras funções como resultado ou mesmo que podemos
    passar funções como argumentos para outras funções, e até mesmo criar
    variáveis do tipo de funções nos nossos programas.

OBS: na seção de funções, nós utilizamos isso.

Em Python, as funções são cidadões de primeira classe, first class citizen

# exemplos - definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(a, b, funcao):
    return funcao(a, b)


# testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested funcions - Funções aninhadas

# Em Python podemos ter também funções dentro de funções, que são conhecidas
# por Nested Functions ou também Inner Functions (funções internas).

# exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Angelina'))
print(cumprimento('Felicity'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahaha', 'kkkkkk', 'yayaya'))
    return rir

rindo = faz_me_rir()
print(rindo())
"""

# inner functions (funções internas / nested functions) podems acessar o escopo
# de funções mais externas.

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kkkkk', 'lololo'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())

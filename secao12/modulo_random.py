"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números
pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste
# Forma 1 - importando todo o módulo (Não recomendado).

import random

# random() -> gera um número pseudo-aleatório entre 0 e 1

# Ao realizar o import de todo o módulo, todas as funções, atributos,
# classes e propriedades que estiverem dentro do módulo ficarão disponíveis
# Ficarão em memoria. Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos
# uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o
# nome do pacote e o nome da função, separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer
# confuso, mas a função random() é apenas uma função dentro do módulo random

# Forma 2 - importando uma função específica do módulo (recomendado)

from random import random

# No import acima, estamos falando:
# Do módulo random, importe a função random.

for i in range(10):
    print(random())

# uniform() -> gerar um número real pseudo-aleatório entre os valores
# estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

# randint() -> gera valores inteiros pseudo-aleatórios entre os valores
# estabelecidos.

# Gerador de apostas para a mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# choice() -> mostra um valor aleatório entre um iterável.

from random import choice

print(choice('Geek University'))
"""

# shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas.pop())

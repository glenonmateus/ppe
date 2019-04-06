"""
Trabalhando com módulos builtin (módulos integrados, que já vem instalados
no Python)

|Python|Módulos Builtin|

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random()))

# podemos importar todas as funçoes de um módulo utilizando o *
from random import *
print(random())

# importando todo o módulo
import random
print(random.random())

# Utilinado alias (apelidos) para módulos/funções
from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())
"""

# costumamos a utilizar tuple para colocar multiplos imports de um mesmo
# módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(3, 7))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('University'))

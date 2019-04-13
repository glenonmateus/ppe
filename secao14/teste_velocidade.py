"""
Teste de velocidade com expressões geradoras

# Generators (Geradores)


def numeros():
    for numero in range(1, 10):
        yield numero


ge1 = numeros()

print(ge1)  # generator

print(next(ge1))
print(next(ge1))


# Generator expression

ge2 = (numero for numero in range(1, 10))

print(ge2)  # generator expression

print(next(ge2))
print(next(ge2))
"""

# realizando o teste de velocidade
import time

# Generator expression
gen_inicio = time.time()
print(sum((numero for numero in range(1, 1000000000))))
gen_tempo = time.time() - gen_inicio

# list comprehension
list_inicio = time.time()
print(sum([numero for numero in range(1, 1000000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}')
print(f'List comprehension levou {list_tempo}')

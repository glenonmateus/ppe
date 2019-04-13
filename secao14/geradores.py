"""
Geradores

- Geradores (Generators) são iterators (iteradores)

OBS: o contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informaçõe:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com expressões geradoras;

Diferenças entre funções e generators functions (funções geradoras)

Funções:
    - utilizam return;
    - retorna uma vez;
    - quando executada, retorna um valor;

Generator functions:
    - utilizam yield;
    - podem utilizar yield múltiplas vezes;
    - quando executada, retorna um generator;

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for numero in gen:
    print(numero)

gen = conta_ate(5)

print(next(gen))  # 1
print()
for numero in gen:
    print(numero)
"""

# Exemplo de Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador < valor_maximo:
        yield contador
        contador += 1


# OBS: uma generator function não é um generator, ela gera um generator
gen = list(conta_ate(5))
print(gen)

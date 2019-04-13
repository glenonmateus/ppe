"""
Teste de memória com generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13 ...

"""

# Função usando listas


def fib_lista(maximo):
    numeros = []
    a, b = 0, 1
    while len(numeros) < maximo:
        numeros.append(b)
        a, b = b, a + b
    return numeros


# Função usando geradores


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador += 1


for numero in fib_gen(10):
    print(numero)

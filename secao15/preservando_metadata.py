"""
Preservando metadatas com wraps

Metadatas -> são dados intrísecos em arquivos.

wraps -> são funções que envolvem elementos com diversas finalidades.

# problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra
        print(f'Você esta chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números
    return a + b


# print(soma(2, 2))
print(soma.__name__)
print(soma.__doc__)
"""

# resolução do problema
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você esta chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(2, 2))
print(soma.__name__)
print(soma.__doc__)

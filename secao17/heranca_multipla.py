"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de
múltiplas classes fazendo com que a classe filha herde todos os atributos e
métodos de todas as classes herdadas

# OBS: a herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;
"""

# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass

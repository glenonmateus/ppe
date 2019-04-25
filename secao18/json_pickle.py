"""
JSON e Pickle

JSON -> JavaScript Objetct Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, YouTube ...) e terceiros (nós, desenvolvedores).

import json

retorno = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2300)}])
print(type(retorno))
print(retorno)

import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)

# Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
ret = jsonpickle.encode(felix)
print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    arquivo.write(jsonpickle.encode(felix))
"""

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = jsonpickle.decode(arquivo.read())
    print(conteudo)
    print(type(conteudo))
    print(conteudo.nome)
    print(conteudo.raca)

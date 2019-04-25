"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo pickle não é seguro contra dados maliciosos e desta forma não
é recomendado trabalhar com arquivos pickle vindos de outras pessoas que você
não conheça ou de fontes desconhecidas.

"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        return f'{self.__nome} está comendo ...'

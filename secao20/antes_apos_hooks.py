"""
Unittest - Antes e após hooks

Hooks - são os testes em si. Ou seja, a execução dos testes.

setup() -> é executado antes de cada método de teste. É util para criarmos
instância de objetos e outros dados;

tearDown() -> É executado ao final de cada método de teste. É útil para excluir
dados ou fechar conexões com bancos de dados.
"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # configurações do tearDown()
        pass
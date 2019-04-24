"""
# Exercicio 1


class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        return f'''{self.__nome} mora no endereço {self.__endereco}
                Telefone para contato: {self.__telefone}'''


pessoa = Pessoa('Glenon', 'Rua Augusto de Lima Junior 19 apto 2', '982091740')
print(pessoa.imprimir())
"""

# Exercicio 3


class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
        self.__area = 0
        self.__perimetro = 0

    def calcular_area(self):
        self.__area = self.__lado ** 2

    def calcular_perimetro(self):
        self.__perimetro = self.__lado * 4

    def imprimir(self):
        return f'''Lado: {self.__lado}
Área: {self.__area}\nPerimetro: {self.__perimetro}'''


quadrado = Quadrado(4)

quadrado.calcular_area()
quadrado.calcular_perimetro()
print(quadrado.imprimir())

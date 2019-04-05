"""
Debuggando com PDB

PDB -> Python Debugger

# OBS: A utilização do print() para debuggar código é uma prática ruim

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar um divisão por Zero'
print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o
# Debugger. Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm
# ou utilizando o PDB.

# Exemplo

from random import randrange

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar um divisão por Zero'

print(dividir(randrange(0, 50), randrange(1, 50)))

# Exemplo com o PDB

# Para utilizar o PDB, precisamos importar a bibioteca pdb e então utilizar a função set_trace()
OBS: A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug
foi incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l - listar onde estamos no código
# n - próxima linha
# p - imprime variável
# c - continua a execução, finaliza a debugging

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início do arquivo.
# Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós
# colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso' + curso
print(final)
"""

# OBS: cuidado com conflitos entre nomes de variáveis e os comandos do pdb
# Como os nomes das variáveis são os mesmos do comando do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja, p nome_da_variável

# Nada de colocar nomes não representativos em variáveis, sempre optar por nomes significativos
"""
Generator Expression

Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

Não vimos:
    - Tuple Comprehension ... porque elas se chamam generators

NOMES = ['Carlos', 'Camila', 'Carla', 'Cassiana', 'Cristiane', 'Vanessa']
print(any(nome[0] == 'C' for nome in NOMES))

# List Comprehension
RES = [nome[0] == 'C' for nome in NOMES]
print(type(RES))
print(RES)

# Generator
RES = (nome[0] == 'C' for nome in NOMES)
print(type(RES))
print(RES)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em
# memória do elemento passdo como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória.
# Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92310230129348))
print(getsizeof(True))
"""

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Set Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dic Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

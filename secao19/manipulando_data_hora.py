"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

2019-04-26 09:28:10.006284
# 5 minutos depois, pode ser ajustado com replace()
2019-04-26 09:33:10.006284

# Recebendo dados do usuário e convertendo para data
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora
print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # horas
print(evento.minute)  # minutos
print(evento.second)  # segundos
print(evento.microsecond)  # microsegundos

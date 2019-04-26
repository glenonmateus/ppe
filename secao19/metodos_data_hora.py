"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (fuso horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana, weekday()
# Os dias da semana do método weekday() começam em zero, sendo esta a segunda-feira
# 0 - segunda-feira (monday)
# 1 - terça-feira (tuesday)
# 2 - quarta-feira (wednesday)
# 3 - quinta-feira (thursday)
# 4 - sexta-feira (friday)
# 5 - sábado (saturday)
# 6 - domingo (sunday)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

aniversario = input('Qual a sua data de nascimento (dd/mm/yyyy): ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
weekdays = ['Segunda-Feria', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
print(f'Você nasceu em um(a) {weekdays[aniversario.weekday()]}')

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

def formata_data(data):
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return f'{data.day} de {months[data.month]} de {data.year}'

import datetime
from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)
nascimento = input('Qual a sua data de nascimento (dd/mm/yyyy): ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)

# Marcando tempo de execução do nosso código com timeit
# loop for
tempo = timeit.timeit('" ".join(str(n) for n in range(100))', number=100000)
print(tempo)
# List Comprehension
tempo = timeit.timeit('" ".join([str(n) for n in range(100)])', number=100000)
print(tempo)
# Map
tempo = timeit.timeit('" ".join(map(str, range(100)))', number=100000)
print(tempo)
"""

import timeit
import functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))

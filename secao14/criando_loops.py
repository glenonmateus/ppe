"""
Criando sua própria versão de loop

for numero in [1, 2, 3, 4, 5]:
    print(numero)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Geek University')


def meu_for(iteravel):
    try:
        it = iter(iteravel)
    except TypeError:
        print('O valor passado não é um iterável')
        return
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5, 6]
meu_for(numeros)

meu_for(1)
"""

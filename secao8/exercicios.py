"""
# Exercicio 1

def dobro(a):
    return a * 2

print(dobro(6))

# Exercicio 2

def data(data):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    datatxt = data.split('/')
    dia = str(datatxt[0])
    mes = str(meses[int(datatxt[1]) - 1])
    ano = str(datatxt[2])
    return f'{dia} de {mes} de {ano}'

print(data('01/01/2000'))
print(data('01/12/2000'))
    """

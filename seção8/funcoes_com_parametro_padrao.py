"""
Funções com Parametro Padrão (default paramters)

- funções onde a passagem de parametro seja opcional

# Exemplo de função onde a passagem de parametro seja opcional

print('Geek University')

print()

# Exemplo de função onde a passagem de parametro seja obrigatória

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  # TypeError


def exponencial(numero=2, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # por padrão eleve ao quadrado
print(exponencial(3, 5))  # eleva a potência informada pelo usuário

# OBS: se o usuário passar somente um parametro, este seja atribuido
# ao parametro número e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parametro
# numero e o segundo ao parametro potencia. Então será calculada esta potência.

print(exponencial())

# OBS: Em funções Python, os parametros com valores default (padrão) DEVEM
# sempre estar ao final da declaração

# Erro!
def test(num=2, potencia):
    return num ** potencia

# Outros exemplos


def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError

# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por que utilizar parametros com valor default?
# - Nos permite ser mais flexíveis nas funções;
# - Evita erros de parametros incorretos;
# - Nos permite trabalhar com exemplo mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores defaul para parametros?
# Qualquer tipo de dados:
# - números, strings, floats, booleanos, litas, tuplas, dicionários,
# funções e etc;

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões ...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: se tivermos uma variável local com o mesmo nome de uma variável
# global, a local terá preferência.


def diz_oi():
    prof = 'Geek'  # variável local
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError
total = 0


def incrementa():
    total = total + 1  # UnboundLocalError (a variável local está sendo
    # utilizada para processamento sem ter sido inicializada).
    return total


print(incrementa())

# ATENÇÃO com variáveis globais (se puder evitar, evite!)

total = 0


def incrementa():
    global total  # avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções,
# e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
print(dentro())  # NameError
"""

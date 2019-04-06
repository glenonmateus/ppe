"""
Funções com Parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
    entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
    - não possuem entrada;
    - não possuem saída;
    - possuem entrada mas não possuem saída;
    - não possuem entrada mas possuem saída;
    - possuem entrada e saída;

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

print(quadrado())  # TypeError


def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Glenon')

# Funções podem ter n parametros de entrada. Ou seja, podemos receber
# como entrada em uma função quantos parametros forem necessários.
# Eles são separados por vírgula.

# Exemplo


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return(num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parametro ou argumentos,
# teremos TypeError
# print(soma(2, 3, 4))  # TypeError - passando argumentos a mais
# print(soma(2))  # TypeError - passando argumentos a menos

# Nomeando paramentros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# Diferença entre parametros e argumentos

# Parametro são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa!

nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# caso utilizemos nomes dos parametros nos argumentos para informá-los
# podemos utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = tuple(lista)
print(soma_impares(tupla))

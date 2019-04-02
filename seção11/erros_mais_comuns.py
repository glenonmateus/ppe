"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela
excução do nosso código

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja,
você escreveu algo que o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError()

a)
def funcao:
    print('Geek University')

b)
None = 1

c)
return

NameError -> ocorre quando um variável ou função não foi definida.

# Exemplos NameError()

a)
print(geek)

b)
geek()

c)
a = 18
if a < 10:
    msg = 'É menor que 10'
print(msg)

TypeError -> ocorre quando uma função/operação/ação é aplicada a um tipo
errado.

# Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

IndexError -> ocorre quando tentamos acessar um elemento em uma lista ou outro
tipo de dado indexado utilizando um índice inválido.

# Exemplos IndexError

a)
lista = ['Geek']
print(lista[1])

b)
lista = ['Geek']
print(lista[0][10])

ValueError -> ocorre quando uma função/operação built-in (integrada) recebe
um argumento com tipo correto mas valor inapropriado.

# Exemplos ValueError

a)
print(int('Geek'))

KeyError -> ocorre quando tentamos acessar um dicionário com uma chave que não
existe

# Exemplos KeyError

a)
dic = {}
print(dic['geek'])

AttributeError -> ocorre quando uma variável não tem um atributo/função.

# Exemplo AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos a indentação do Python
(4 espaços)

# Exemplo IndentationError

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1

OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante ler e prestar atenção na saída de erro.
"""

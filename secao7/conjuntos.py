"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria
dos conjuntos da matemática

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não
nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves,
valores e itens duplicados

Os conjuntos (Sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados não temos ordem

dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

# Lista aceita valores duplicados, então temos 10 elementos
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# Tupla aceita valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionario não aceita chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjunto não aceita valores duplicados, então temos 8 elementos
conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# Informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em um lista python, á que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidade distintas, ou seja, únicas, temos.
# O que você faria? faria um loop na lista ... ?
# Podemos utilizar o set para isso
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é indice! Informamos o valor a ser removido. nenhum valor é retornado.
print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro keyerror.

# Forma 2
s.discard(2)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conunto para outro ...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens do conjunto
s.clear()
print(s)

# Métodos matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python
# e um contendo estudantes do curso Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam python também estudam java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - Utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, valor máximo, valor mínimo, tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

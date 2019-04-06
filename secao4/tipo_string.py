"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

    - Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
    - Estiver entre aspas duplas 
    - Estiver entre aspas simples triplas 
    - Estiver entre aspas simples triplas

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar" 
print(nome)
print(type(nome))

nome = 'Angelina \nJolie' # \n nova linha
print(nome)
print(type(nome))

nome = "Anjelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())
print(nome.lower())
print(nome.split()) # Transforma em uma lista de strings
print(nome[0:4]) # slice de string
print(nome[5:15]) # slice de string
print(nome.split()[0])
print(nome.split()[1])
"""

# [ 0,  1,  2,  3, ... ]
# ['G','e','e','k', ...]
nome = 'Geek University'
"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta (inverte string)
"""
print(nome[::-1])
print(nome.replace('e', 'i'))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)
print(texto[::-1])

nome = 'ana' # Palíndromo
print(nome)
print(nome[::-1])

"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.
Ela recebe um parâmetro que indica onde queremos coloar o cursor

arquivo = open('texto.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read())

arquivo.seek(22)
print(arquivo.read())

# readline() -> função que lê o arquivo linha a linha

arquivo = open('texto.txt')
print(arquivo.readline())
print(type(arquivo.readline()))
print(arquivo.readline().split(' '))

# readlines() ->

linhas = len(arquivo.readlines())
print(linhas)

print(arquivo.readlines())

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre
o arquivo no disco do computador e o nosso programa. Essa conexão é chamada de
streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão
Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo
2 - Trabalhar o arquivo
3 - Fechar o arquivo

# 1 - Abrir o arquivo
arquivo = open('texto.txt')
# 2 - Trabalhar o arquivo
print(arquivo.read())
print(arquivo.closed)  # verifica se o arquivo está aberto ou fechado.
# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um
# ValueError
"""

arquivo = open('texto.txt')
# com a função read() podemos limitar a quantidade de caracteres a serem lidos
# no arquivo.
print(arquivo.read(50))

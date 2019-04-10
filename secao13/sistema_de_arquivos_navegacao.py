"""
Sistema de arquivo e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do módulo 'os'.

os -> operating system - sistema operacional

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# retorna o path (caminho) absoluto.
print(os.getcwd())

# para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/glenonmateus/'))

import os

# Podemos identificar o sistema operacional com o módulo 'os'
print(os.name)  # posix (linux ou mac), nt (windows)

# podemos ter mais detalhes no sistema operacional
print(os.uname())

import sys
print(sys.platform)

print(os.getcwd())  # /file/glenonmateus/git/ppe/secao13
print(os.path.join(os.getcwd(), 'geek'))  # /file/glenonmateus/git/ppe/secao13/geek

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o
# diretório atual e o segundo o diretório que será juntado ao atual.

# podemos listar os arquivos e diretórios com os listdir()

print(os.listdir('..'))
"""

import os

# podemos listar os arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir()
arquivos = list(scanner)
# print(arquivos)
print(arquivos[0].name)  # nome do arquivo
print(arquivos[0].inode())
print(arquivos[0].is_dir())  # é um diretório? False
print(arquivos[0].is_file())  # é um arquivo? True
print(arquivos[0].is_symlink())  # é um link simbólico? False
print(arquivos[0].path)  # caminho até o arquivo
print(arquivos[0].stat())  # estatisticas sobre o arquivo

# OBS: quando utilizamos a função scandir() nós precisamos fechá-la. Assim
# quando abrimos um arquivo
scanner.close()

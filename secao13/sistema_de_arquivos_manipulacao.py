"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# arquivo
print(os.path.exists('outro.txt'))  # True

# diretório
# paths relativos
print(os.path.exists('geek/university'))  # False
# paths absolutos
print(os.path.exists('/home/glenonmateus/git/ppe'))

# criando arquivos
# forma 1
open('arquivo-teste1.txt', 'w').close()
# forma 2
open('arquivo-teste2.txt', 'a').close()
# forma 3
with open('arquivo-teste3.txt', 'a') as arquivo:
    pass

# recomendado
os.mknod('arquivo-teste4.txt')
os.mknod('/home/glenonmateus/arquivo-teste5.txt')
# OBS: se você estiver utilizando no MacOS, pode haver um erro de
# PermissionError
# OBS: criando um arquivo via mknod(), se o arquivo já existir teremos o erro
# FileExistsError

# criando diretórios - únicos (um a um)
os.mkdir('templates')
# OBS: a função mkdir() cria um diretório se este não existir. Caso exista,
# teremos FileExistsError

os.mkdir('/etc/templates')
# OBS: se não tivermos permissão para criar o diretório teremos um
# PermissionError

# criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university')
# OBS: se já existir, teremos FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# renomear arquivos e diretórios
os.rename('templates2', 'geek2')
# OBS: se o diretório não existir teremos FileExistsError
# OBS: se o diretório que queremos renomear não estiver vazio, teremos um
# OSError

# Atenção! tome cuidado com os comandos de deleção. Ao deletarmos um arquivo
# ou diretório, eles não vão para a lixeira.
# removendo arquivos
os.remove('geek.txt')
# OBS: se você estiver no windows e o arquivo que você for deletar estiver em
# uso, você terá um erro.
# OBS: caso o arquivo não exista teremos um FileNotFoundError
# OBS: se você informar um diretório ao invés de um arquivo, teremos um
# IsADirectoryError

# removendo diretórios vazios
os.rmdir('templates/geek/university')
# OBS: Se o direrótio tiver qualquer conteúdo teremos um OSError
# OBS: se o diretório não existir teremos um FileExistsError

# removendo vários arquivos em um diretório
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# podemos remover um árvore de diretórios vazios
os.removedirs('geek2/novo2')
# se algum dos diretórios contiver arquivos ou outros diretório, o processo
# para.

# envia arquivos e diretórios para a lixeira
from send2trash import send2trash
send2trash('frutas.txt')
# OBS: se o arquivo não existir, teremos OSError

# criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')

# estamos criando um diretório temporário, abrindo o mesmo e dentro dele
# criando um arquivo para escrevermos um texto. No final, usamos um input()
# só para mantermos os arquivos temporários 'vivos' dentro dos blocos with

# OBS: possivelmente, o código acima não irá funcionar se você estiver
# utilizando o Windows. Por conta desse sistema trbalhar de forma diferente
# com arquivos temporários.

# criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: em arquivos temporários só conseguimos escrever bits. Por isso,
# utilizamos b''
"""

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

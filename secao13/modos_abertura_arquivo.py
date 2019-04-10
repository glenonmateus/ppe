"""
Modos de abertura de arquivo

r -> abre modo leitura (padrão)
w -> abre modo escrita (sobrescreve caso o arquivo já exista)
x -> abre modo escrita somente se o arquivo não existir. Caso o arquivo exista,
gera FileExistsError
a -> abre modo escrita adicionando o conteúdo ao final do arquivo.
+ -> abre modo atualização: leitura e escrita (temos o controle do cursor)

OBS: abrindo no modo 'a', se o arquivo não existir será criado, caso exista o
novo conteúdo será adicionado sempre ao final. Com o modo 'a', não controlamos
o cursor.

# Exemplo 'x'
with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')

# Exemplo 'a'
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""

with open('outro.txt', 'a+') as arquivo:
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')

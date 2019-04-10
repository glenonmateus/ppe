"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura não podemos realizar a escrita nele.
Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos
lê-lo, somente escrever nele.

# OBS: ao abrir um arquivo para escrita, o arquivo é criado no sistema
operacional

Para escrevermos dados em um arquivo, após abrir um arquivo utilizamos a função
write(), esta função recebe uma string como parâmetro, caso contrário teremos
um TypeError.

Abrindo um arquivo para escrita com o modo 'w' se o arquivo não existir será
criado, caso ele já exista, o anterior será apagado e um novo será criado.
Dessa forma, todo o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos\n')
    arquivo.write('Mais esta é a última linha.')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> gera um objeto para que possamos escrever em um arquivo CSV
# Utilizamos o método writerow() para escrever cada linha. Este método recebe
# uma lista
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informa a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""

# DicWriter
# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho
from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while True:
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme: ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
        else:
            break

"""
Dicionários

OBS: Em algumas linguagens de programação, os dicinários Python
são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

indice -> [0, 1, 2]
listas -> [1, 2, 3]

OBS: Sobre dicionários
 - Chave e valor são separados por dois pontos 'chave:valor'
 - tanto chave quanto valor podem ser de qualquer tipo de dado
 - podemos misturar tipos de dados

# Criação de dicionários
# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos',
          'py': 'Paraguai'}
print(paises)
print(type(paises))
# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe
# teremos o erro KeyError
# Forma 2 - Acessando via get - recomendada
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado
# o valor None e não será gerado KeyError
pais = paises.get('ru')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a
# chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais}')
"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos',
          'py': 'Paraguai'}

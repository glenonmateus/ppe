"""
Len, Abs, Sum, Round

len() -> retorna o tamanho (ou seja, o número de itens) de um iterável
"""

# Só pra revisar

print(len('Geek University'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o
# seguinte

# Dunder len
print('Geek University'.__len__())

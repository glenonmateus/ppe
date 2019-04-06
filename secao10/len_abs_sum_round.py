"""
Len, Abs, Sum, Round

len() -> retorna o tamanho (ou seja, o número de itens) de um iterável

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

abs() -> retorna o valor absoluto de um número inteiro ou real. De forma básica
seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial,
e retorna a soma total dos elementos, incluindo o valor

OBS: o valor inicial default = 0

# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.145, 5.678]))
print(sum([(1, 2, 3, 4, 5)]))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'c': 5}.values()))

round() -> retorna um número arredondado para n digito de precisão após a casa
decimal. Se a precisao não for informada retorna o inteiro mais próximo da
entrada.

# Exemplos round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121212, 2))
print(round(1.21999999999, 2))
"""

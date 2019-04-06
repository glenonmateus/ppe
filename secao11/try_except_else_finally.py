"""
Try, Except, Else, Finally

Dica de quando e onde tratar código

TODA ENTRADA DEVE SER TRATADA!

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError as e:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou para desalocar recursos.

# Exemplo mais complexo
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!
"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar um divisão por Zero'

    # except (ValueError, ZeroDivisionError) as err:
    #    return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

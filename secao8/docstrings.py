"""
Documentando funções com Docstrings

OBS: Podemos acessar uma função em Python utilizando
a propriedade especial __doc__

Podemos acessar a documentação com a função help()
"""

# Exemplos


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi! '


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quardado de 'numero'
    ou o 'numero' a 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencial: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

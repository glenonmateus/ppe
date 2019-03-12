"""
Escopo de variáveis

Dois casos de escopo:

    1 - Variáveis globais:
        - Variáveis globais são reconhecidas, ou seja, seu escopo compreendetodo o programa

    2 - Variáveis locais:
        - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada

Para declarar variáveis em Python fazemos:

    nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dados dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
    int numero = 42;

Exemplo em Java:
    int numero = 42;
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 1 
if numero > 10:
    novo = numero + 10 # variável 'novo' está declarada localmento dentro do block do if. Portanto, é local
    print(novo)

print(novo)

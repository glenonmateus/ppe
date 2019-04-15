"""
Decoradores (decorators)

O que são decorators?
    - decorators são funções;
    - decorators envolvem outras funções e aprimoram seus comportamentos;
    - decorators também são exemplos de Higher Order Functions;
    - decorators tem uma sintaxe própria, usando "@" (syntact sugar)


# decorators como funções (sintaxe não recomendada)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


seja_educado(saudacao)()


def raiva():
    print('EU TE ODEIO!')


seja_educado(raiva)()

# decorators com Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir ...')


dormir()
"""

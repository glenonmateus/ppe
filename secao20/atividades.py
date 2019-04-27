def comer(comida, eh_saudavel):
    if eh_saudavel:
        return f'Estou comendo {comida} porque quero manter a forma.'
    return f'Estou comendo {comida} porque a gente só vive uma vez.'


def dormir(numero_horas):
    if numero_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    return f'Continuo cansado após dormir por {numero_horas} horas.'


def eh_engracado(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

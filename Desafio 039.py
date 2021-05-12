# Faça um programa que leia o ano de nascimento de um jovem e mostre de acordo com a sua idade
# se ele ainda vai se alistar no exercito, se é hora de se alistar ou se passou o tempo de alistamento.
from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today()
ano_atual = ano_atual.year
idade = ano_atual - ano_nascimento
if idade == 18:
    print('Você tem 18 anos e deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você tem {} anos, o seu tempo de se alistar já passou!'.format(idade))
    ano = ano_nascimento + 18
    print('Você deveria se alistar em {}'.format(ano))
elif idade < 18:
    print('Você tem {} anos'.format(idade))
    print('Você aida é menor de idade!')
    ano = ano_nascimento + 18
    print('Você vai se alistar em {}'.format(ano))

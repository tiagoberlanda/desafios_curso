# Faça um programa que leia o ano de nascimento de um jovem e mostre de acordo com a sua idade
# se ele ainda vai se alistar no exercito, se é hora de se alistar ou se passou o tempo de alistamento.
# o programa deve mostar o tempo que falta ou o tempo que passou.
idade = int(input('Digite a sua idade: '))
if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade < 18:
    print('Faltam {} anos para você se alistar!'.format(18 - idade))
else:
    print('Já se passaram {} anos do seu alistamento.'.format(idade - 18))

# Crie um programa que leia o ano de nascimento de um atleta e moste
# sua categoria de acordo com a idade
#até 9(mirim), até 14(infantil),até 19(junior),até 20(senior), acima(master)

from datetime import date # bibilioteca para verificar a data atual

data_atual = date.today().year # definindo o ano atual 

nascimento = int(input('Digite em que ano você nasceu: '))
ano = data_atual - nascimento

if ano < 9:
    print('Categoria Mirim!')
elif ano > 9 and ano <= 14:
    print('Categoria infantil!')
elif ano > 14 and ano < 19:
    print('Categoria junior!')
elif ano <= 19 and ano <= 20:
    print('Categoria Senior!')
else:
    print('Categoria master!')

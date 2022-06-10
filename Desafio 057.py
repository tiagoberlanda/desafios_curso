print ('''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores
M ou F, Caso esteja errado peça a digitação novamente até ter um valor válido''')

condicao = 0
while condicao == 0:
    sex = str(input('Digite o Sexo [M] ou [F]:\n')).upper()
    if (sex == 'M' or sex == 'F'):
        print('Você digitou um valor válido.\nEncerrando...')
        condicao = 1
        
    else:
        print('Você digitou um valor inválido, tente novamente!')

print('Fim')

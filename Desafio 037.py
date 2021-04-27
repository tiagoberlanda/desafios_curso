# Escreva um programa que leia um número inteiro e peça para o usuário escolher
# qual será sua base de conversão.
print('Digite o valor e qual a sua base de conversão!')
valor = int(input('Digite um valor inteiro: '))
teste = int(input('[1] para Binário\n[2] para Octal\n[3] para Hexadecimal\n'
'[4] Sair\n'))
if teste == 1:
    print('{} em binário é igual a {}'.format(valor,bin(valor)[2:]))
elif teste == 2:
    print('{} em octal é {}'.format(valor,oct(valor)[2:]))
elif teste == 3:
    print('{} em hexadecimal é {}'.format(valor,hex(valor)[2:]))
else:
    exit()
print('Fim do programa!')

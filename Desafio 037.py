# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será sua base de conversão.
import math
print('Digite o valor e qual a sua base de conversão!')
teste = int(input('[1] para Binário\n[2] para Octal\n[3] para Hexadecimal\n[4] Sair\n'))
valor = int(input('Digite um valor inteiro: '))
if teste == 1:
    binario = bin(valor)
    print('{} em binário é igual a {}'.format(valor,binario))
elif teste == 2:
    octal = oct(valor)
    print('{} em octal é {}'.format(valor,octal))
elif teste == 3:
    hexadecimal = hex(valor)
    print('{} em hexadecimal é {}'.format(valor,hexadecimal))
else:
    exit()
print('Fim do programa!')

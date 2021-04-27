# Crie um programa que leia um número real e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número real para saber sua parte inteira: '))
print('A parcela inteira no número {} é {:.0f}'.format(num, trunc(num)))

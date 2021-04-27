# Faça um programa que leia 3 números e diga qual o maior e qual o menor.
cor = {'limpa': '\033[m',
       'verde': '\033[32m',
       'azul': '\033[36m'}
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}{}{}'.format(cor['verde'], menor, cor['limpa']))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O Maior valor digitado foi {}{}{}'.format(cor['azul'], maior, cor['limpa']))

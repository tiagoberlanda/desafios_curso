# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
cor = {'limpa': '\033[m',
       'vermelho': '\033[31m',
       'verde': '\033[32m'}
print('Digite um número para saber seu antecessor e sucessor!')
n1 = int(input('Digite um número: '))
print('O antecessor de {} é {}{}{} e seu sucessor é {}{}{}'.format(n1, cor['vermelho'], n1 - 1, cor['limpa'],
                                                                   cor['verde'], n1 + 1, cor['limpa']))

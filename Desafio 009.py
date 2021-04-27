# Faça um programa que leia um número e mostre a sua tabuada.
n = int(input('Digite um número para saber sua tabuada: '))
n1 = 1
print('-' * 13)
while n1 <= 10:
    print('{} x {:2} = {}'.format(n, n1, n * n1))
    n1 = n1 + 1
print('-' * 13)

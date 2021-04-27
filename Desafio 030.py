# Faça um programa que leia um número qualquer e mostre se ele é impar ou par
num = int(input('Digite o número: '))
par = num % 2
if par == 0:
    print('O valor digitado é par!')
else:
    print('O valor digitado é impar!')

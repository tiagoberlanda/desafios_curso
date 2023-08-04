#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input('Digite um número: '))
total = 1
while numero >= 1:
    print(numero, end='X')
    total = total * numero
    numero = numero - 1
print('\nTotal: ',total)

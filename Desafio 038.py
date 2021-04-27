# Escreva um programa que leia dois valores inteiros e compare-os
# exibindo na tela qual é menor, maior ou igual.
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor2 > valor1:
    print('O Segundo valor é maior')
else:
    print('Os valores são iguais')

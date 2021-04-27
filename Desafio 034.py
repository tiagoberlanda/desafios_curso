# Escreva um programa que leia o salario de um funcionário e calcule um aumento de 10% para valores maiores que
# 1250,00 , valores menores tem um aumento de 15%
salario = float(input('Digite o salário: '))
if salario > 1250.00:
    aumento = (salario * 10) / 100
    print('Seu novo salário é R${}'.format(salario + aumento))
else:
    aumento = (salario * 15) / 100
    print('Seu novo salário é R${}'.format(salario + aumento))

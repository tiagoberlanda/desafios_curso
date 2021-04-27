# Faça um algoritimo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Qual o salário do funcionário? R$'))
aumento = (salario * 15) / 100
print('Seu novo salário é {:.2f}R$'.format(salario + aumento))

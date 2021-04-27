# Faça um programa que leia o nome de uma pessoa e mostre o primeiro nome de uma pessoa e mostre seu
# primeiro e ultimo nome
n = str(input('Digite seu nome completo: ')).strip().upper()
print('Muito prazer em te conhecer',n)
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome) - 1]))

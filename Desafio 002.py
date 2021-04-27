# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas.
cores = {'limpa':'\033[m',
         'azul':'\033[34m'}
nome = input('Digite seu nome: ')
# print('É um grande prazer te conhecer', nome)
print('È um prazer te conhecer {}{}{}!'.format(cores['azul'], nome, cores['limpa']))


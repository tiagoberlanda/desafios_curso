# Crie um programa que leia o nome de uma pessoa e mostre
# O nome com todas as letras maiusculas e minusculas
# Quantas letras tem sem considerar os espaços
# quantas letras tem o primeiro nome
nome = input('Qual o seu nome completo? Meu nome é ').strip()
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
print('Seu nome em minusculo fica {}'.format(nome_maiusculo))
print('Seu nome em maiusculo fica {}'.format(nome_minusculo))
total_sem_espaco = len(nome.replace(' ', ''))
print('Total de letras sem espaço {} letras'.format(total_sem_espaco))
total_primeiro_nome = nome.split()
print('Total de letras do primeiro nome é {} e possui {} letras'.format(total_primeiro_nome[0],
                                                                        len(total_primeiro_nome[0])))

# Faça um programa que leia o nome de uma pessoa e mostre se ela tem silva no nome
nome = input('Digite seu nome: ').strip()
lista = nome.upper().split()
print('Seu nome tem silva? ')
achei = bool(False)
for n in lista:
    if n == 'SILVA':
        achei = True
if achei:
    print('Sim')
else:
    print('Não')

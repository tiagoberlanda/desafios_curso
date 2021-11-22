# Crie um programa que leia umao ano de nascimento de sete pessoas.
# Depois motre quantas pessoas ainda não atingiram a maioridade e quantas já são de
from datetime import date
data = date.today()
ano = data.year

menor = 0
maior = 0
for c in range(0,7):
    pessoa = int(input('Digite o ano de nascimento da pessoa:'))
    idade = ano - pessoa
    if idade < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('Tem {} pessoas maiores de idade e {} menores de idade'.format(maior, menor))


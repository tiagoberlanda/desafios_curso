# Faça um programa que leia um ano e diga se ele é bissexto ou não.
cores = dict(limpa='\033[m', verde='\033[32m', vermelho='\033[31m')
from datetime import date
print('Digite um ano para saber se ele é bissexto ou não!')
ano = int(input('Digite o ano, coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}Sim{}, {} é um ano bissexto!'.format(cores['verde'], cores['limpa'], ano))
else:
    print('{}Não{}, {} não é bissexto!'.format(cores['vermelho'], cores['limpa'], ano))

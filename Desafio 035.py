# Faça um programa que leia 3 valores e diga se é possível que elas formem um triângulo ou não
cor = {'limpa': '\033[m',
       'vermelho': '\033[1;31m',
       'verde': '\033[1;32m'}
print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima {}PODEM{} formar um triângulo!'.format(cor['verde'], cor['limpa']))
else:
    print('Os Segmentos acima {}NÃO PODEM{} formar um triângulo!'.format(cor['vermelho'], cor['limpa']))

# Faça um programa que o computador pense em um número entre 1 e 5 e peça para o usuário tentar acertar
# O programa deverá dizer se você acertou ou não
from random import randint
from playsound import playsound
from time import sleep
print('-=-' * 20)
print('Estou pensando em um número entre 1 e 5, tente adivinhar!')
print('-=-' * 20)
chute = int(input('Qual o seu palpite: '))
print('Processando...')
sleep(2)
aleatorio = randint(1, 5)
if chute == aleatorio:
    print('Parabéns você acertou!')
    print('Estava pensando no número {} mesmo!'.format(aleatorio))
    playsound('Acertou.mp3')
else:
    print('Errou, o computador ganhou!')
    print('Estava pensando no número {}!'.format(aleatorio))
    playsound('Errou.mp3')

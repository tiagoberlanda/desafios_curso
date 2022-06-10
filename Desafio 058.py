print ('''Melhore o jogo do Desafio 028 onde o computador vai pensar em um número
entre 0 e 10, só que agora o jogador vai tentar adivinhar até certarm mostrando no final
quantos palpites foram necessários para vencer''')
from random import randint
from time import sleep

print('-=-' * 20)
print('Estou pensando em um número entre 1 e 10, tente adivinhar!')
print('-=-' * 20)

condicao = 0
aleatorio = randint(1, 10)
contagem = 1

while condicao == 0:
    chute = int(input('Qual o seu palpite: '))
    print('Processando...')
    sleep(1)
    if chute == aleatorio:
        print('Parabéns você acertou!')
        print('Estava pensando no número {} mesmo!'.format(aleatorio))
        print('Tentativas: {}'.format(contagem))
        condicao = 1
    
    else:
        print('Errou, o computador ganhou!\nTente Novamente!')
        contagem += 1
print('Fim')

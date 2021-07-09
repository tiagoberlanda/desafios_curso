#Crie um programa que faça o computador jogar jokenpô com você
from random import randint      #Biblioteca para gerar números aleatorios inteiros
computador = randint(1,3)   # Define o range de valores inteiros

print('Vamos jogar Pedra, Papel e Tessoura, bora?')
menu = ('[1] = Pedra \n[2] = Papel \n[3] = Tessoura')
print (menu)
chute = int(input('Escolha: '))

if chute > 3:
    print('Opção Inválida, o programa será encerrado.')
    exit()

# Mostra o chute do computador
if computador == 1:
    print('3... 2.... 1... eu escolho PEDRA')
if computador == 2:
    print('3... 2... 1... eu escolho PAPEL')
if computador == 3:
    print('3... 2... 1... eu escolho TESSOURA')

# Testar se o computador e o chute foram iguais
if computador == chute:
    print('Pensamos igual, essa não Valeu!')

# Se o computador colocar pedra e o usuario papel 
elif computador == 1 and chute == 2:
    print('Você ganhou, papel enrola a Pedra!')
    
# Se o computador colocar pedra e o usuario Tessoura
elif computador == 1 and chute == 3:
    print('Eu ganhei, pedra esmaga a Tessoura')

# Se o computador colocar papel e o usuario pedra
elif computador == 2 and chute == 1:
    print('Eu ganhei, papel enrola a Pedra!')

# Se o computador colocar papel e o usuario Tessoura
elif computador == 2 and chute == 3:
    print('Você ganhou! Tessoura corta o Papel')
    
# Se o computador colocar Tessoura e o usuario pedra 
elif computador == 3 and chute == 1:
    print('Você ganhou, pedra esmaga a Tessoura')
    
# Se o computador colocar Tessoura e o usuario Papel
elif computador == 3 and chute == 2:
    print('Eu ganhei, tessoura corta o papel')


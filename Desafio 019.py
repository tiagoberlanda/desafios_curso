# Um professor quer sortear um dos 4 alunos para apagar o quadro, faça um programa que ajude ele escrevendo o nome
# do aluno escolhido
from random import choice
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto aluno: ')
sorteado = [a1, a2, a3, a4]
print('O Aluno(a) escolhido foi {}'.format(choice(sorteado)))

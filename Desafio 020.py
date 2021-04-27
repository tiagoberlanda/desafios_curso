# o Professor quer sortear a ordem de apresentação dos alunos, faça um programa que ajude ele
from random import shuffle
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é\n{}'.format(lista))

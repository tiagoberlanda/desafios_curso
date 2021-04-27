# Faça um programa que leia uma frase e mostre o seguinte.
# quantas vezes apareceu a letra 'A'
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez
nome = str(input('Digite uma frase: ')).strip().upper()
qnt = nome.count('A')
print('A quantidade de A nessa frase é {}'.format(qnt))
inicio = (nome.find('A') + 1)
print('O primeiro A foi na posição {}'.format(inicio))
final = (nome.rfind('A') + 1)
print('A ultima posição da letra A foi {}'.format(final))

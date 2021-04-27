# Crie um programa que leia dois números e mostre a soma entre eles.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'f.amarelo': '\033[1;30;43m'}
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'
      .format(cores['azul'], n1, cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['f.amarelo'],
              n1 + n2, cores['limpa']))

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
cor = {'limpa': '\033[m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'branco': '\033[30m',
       'verde': '\033[32m',
       'ciano': '\033[36m',
       'cinza': '\033[37m',
       'fundovermelho': '\033[41m'}
n = input('Digite algo: ').strip()
print('{} é do tipo primitivo {}{}{}'.format(n, cor['fundovermelho'], type(n), cor['limpa']))
lower = n.islower()
up = n.isupper()
alphanum = n.isalnum()
letra = n.isalpha()
space = n.isspace()
numero = n.isnumeric()
decimal = n.isdecimal()
digito = n.isdigit()
capitalize = n.istitle()
print('{} é tudo maiusculo? {}{}{}'.format(n, cor['amarelo'], up, cor['limpa']))
print('{} é tudo minusculo? {}{}{}'.format(n, cor['vermelho'], lower, cor['limpa']))
print('{} é alfanumérico? {}{}{}'.format(n, cor['azul'], alphanum, cor['limpa']))
print('{} é alfabético? {}{}{}'.format(n, cor['roxo'], letra, cor['limpa']))
print('{} é um espaço? {}{}{}'.format(n, cor['branco'], space, cor['limpa']))
print('{} é um número? {}{}{}'.format(n, cor['verde'], numero, cor['limpa']))
print('{} é um dígito? {}{}{}'.format(n, cor['ciano'], digito, cor['limpa']))
print('{} está capitalizada? {}{}{}'.format(n, cor['cinza'], capitalize, cor['limpa']))

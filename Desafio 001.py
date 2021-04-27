# Crie um programa que escreva Olá Mundo na Tela
cores = {'amarelo': '\033[33m',  # Definindo uma lista de cores
         'limpa': '\033[m'}
print('{}Olá, Mundo!{}'.format(cores['amarelo'], cores['limpa']))

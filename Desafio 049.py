# Refaça o desafio 009 mostrando a tabuada porem utilizando o for
numero = int(input('Digite um número para saber sua tabuada: '))
for c in range(1,11):
    print('{} x {} = {}'.format(numero, c,numero*c))
print('Fim')

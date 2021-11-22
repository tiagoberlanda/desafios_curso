# Crie um programa que leia o prum número inteiro e diga se ele é ou não é primo.
n = int(input("Verificar numeros primos ate: "))
tot = 0 

for c in range (1, n + 1):
    if n % c ==0:
        print('\033[33m', end=" ")
        tot += 1
    else:
        print('\033[31m',end=" ")
    print('{}'.format(c), end="")
print('\n\033[mO número {} foi divisível {} vezes.'.format(n,tot))
if tot ==2:
    print('OU seja ele É PRIMO!')
else:
    print('Ou seja o Número NÃO É PRIMO!')

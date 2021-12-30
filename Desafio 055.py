# Crie um programa que leia o peso de 5 pessoas
# depois mostre quem tem o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}KG e o menor foi de {}KG'.format(maior, menor))

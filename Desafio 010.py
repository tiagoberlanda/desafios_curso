# Faça um programa que leia quanto de dinheiro uma pessoa tem e quantos dolares ela pode comprar
# Considerar dolar = 3,27
valor = float(input('Digite quando dinheiro você possui: '))
dolar = valor / 3.27
print('Dá para comprar {:.2f} dolares'.format(dolar))

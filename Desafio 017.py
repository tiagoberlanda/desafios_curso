# Faça um programa que calcula o cateto oposto e adjacente e mostre a hipotenusa.
from math import pow, sqrt, hypot
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
# hipotenusa = sqrt((pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A Hipotenusa vale {:.2f}'.format(hipotenusa))

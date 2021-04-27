# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = int(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
print('O Ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O Ângulo de {} tem o Cosseno de {:.2}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O Ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))

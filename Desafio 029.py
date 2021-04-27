# Faça um programa que leia a velocidade de um carro e se ele estiver acima de 80 KM/H diga que ele foi multado.
# Calcule a multa considerando R$7,00 a cada KM acima do limite
velocidade = int(input('Qual a velocidade do veículo? '))
limite = int(80)
if velocidade < limite + 1:
    print('Sua velocidade está OK, boa viajem!')
else:
    print('Você está {}KM/H acima do limite'.format(velocidade - limite))
    print('Você vai receber uma multa de R${}'.format((velocidade - limite) * 7))

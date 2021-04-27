# Faça um programa que leia a largua de uma parede e calcula a area e a quantidade de tinta necessária para pinta-la
# Considerar 2m² de tinta
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('A área da parede é de {}m² são necessário {:.2f} litros de tinta'.format(area, area / 2))

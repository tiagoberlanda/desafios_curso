# Faça um programa que leia o preço de um produto e mostre seu valor com 5% de desconto
produto = float(input('Digite o valor do produto: '))
desconto = (produto * 5) / 100
print('O valor com desconto fica {}R$'.format(produto - desconto))

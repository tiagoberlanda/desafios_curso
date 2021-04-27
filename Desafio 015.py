#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos,
#  quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos? '))
valor_dias = dias * 60
valor_km = km * 0.15
print('O total a ser pago é de R${}'.format(valor_km + valor_dias))

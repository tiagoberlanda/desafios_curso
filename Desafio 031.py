# Crie um programa que pergunte a distância da viajem em KM e calcule o preço considerando o seguinte.
# até 200 KM é R$0,50 por KM, acima disso é R$0,45.
viagem = float(input('Qual a distância da viagem? Em KM '))
'''if viagem > 200:
    print('O valor da viagem é de R${:.2f}'.format(viagem * 0.45))
else:
    print('O valor da viagem é de R${:.2f}'.format(viagem * 0.50))'''
# Outra Forma de Fazer
preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('O valor total é de R${}'.format(preco))

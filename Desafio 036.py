# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Cacula o valor da prestação mensal sabendo que ela não pode exeder 30% do salário ou então o empréstimo
# será negado.
print('-=-' * 25)
print('Digite as informações solicitadas para simular seu financiamento!')
print('-=-' * 25)
salario = float(input('Digite se salário R$ '))
valor_imovel = float(input('Digite o valor do imóvel R$ '))
prazo = int(input('Digite em quantos anos você pretende pagar: '))
prazo_mensal = prazo * 12
parcela_imovel = valor_imovel / prazo_mensal
salario_30porcento = salario * 30/100
if salario_30porcento >= parcela_imovel:
    print('Seu financiamento foi APROVADO!')
    print('Em {} parcelas de R${:.2f} mensais'.format(prazo_mensal,parcela_imovel))
else:
    print('O valor da parcela mensal ficaria em {:.2f} que é maior que 30% do seu salário'.format(parcela_imovel))
    print('Seu financiamento foi REPROVADO!')

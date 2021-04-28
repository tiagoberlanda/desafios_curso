# Escreva um programa que calcula o valor a ser pago por um produto considerando
# o seu preço normal
# e condição de pagamento.
# a vista dinheiro/cheque: 10% de desconto
# a vista cartao: 5% de desconto
# ate 2x no cartao: preço normal
# 3x ou mais no cartao: 20% de juro
#Definindo o preço do produto, solicitando ao usuário.
preco_produto = float(input('Digite o valor do produto, R$'))
forma_pagamento = int(input('''[1] para DINHEIRO/CHEQUE
[2] para A VISTA NO CARTÃO\n[3] para 2X no CARTAO
[4] para 3X ou MAIS no CARTAO\n'''))
# Definindo variáveis de deconto e juros 
desconto_avista_dinheiro = preco_produto * 10 / 100     # desconto 10%
desconto_avista_cartao = preco_produto * 5 / 10       # desconto 5%
juro_cartao = preco_produto * 20 / 100        # juros 20%
# Testa as condição conforme digitado pelo usuário
if forma_pagamento == 1:  
    print('O valor do produto na condição escolhida com desconto é de R${}'
    .format(preco_produto - desconto_avista_dinheiro))     
elif forma_pagamento == 2:
    print('O valor do produto na condição escolhida com desconto é de R${}'
    .format(preco_produto - desconto_avista_cartao))
elif forma_pagamento == 3:
    print('2 X no CARTAO não tem desconto!')
    print('O valor do produto na condição escolhida é de R${}'
    .format(preco_produto))
elif forma_pagamento == 4:
    print('Essa condição de pagamento possui juros!')
    print('O valor do produto na condição escolhida com juros é de R${}'
    .format(preco_produto + juro_cartao))
else:
      # Tratativa de erro caso o usuário digite uma opção inválida.
    print('Você escolheu uma opção inválida, tente novamente.')
    
print('Fim do Programa.')

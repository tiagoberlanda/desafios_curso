# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com SANTO
cidade = input('Digite o nome da cidade: ').strip()
teste = cidade.upper().split()
if teste[0] == 'SANTO':
    print('Sim, começa com SANTO')
else:
    print('Não, não começa com SANTO')
print(teste)
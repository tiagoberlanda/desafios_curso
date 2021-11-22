# Crie um programa que leia o primeiro termo e a razão de uma PA.
# No final mostre os 10 primeiros termos dessa progressão

termo = int(input('Digite o termo da PA: '))
progressao = int(input('Digite a progressão da PA: '))
decimo = termo + (10 - 1) * progressao
print("Os primeiros termos dessa progressão são:")
for c in range(termo, decimo + progressao, progressao):
    print(c, end=' -> ')

print('Acabou')

# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando o While.
termo = int(input('Digite o termo da PA: '))
progressao = int(input('Digite a progressão da PA: '))
decimo = termo + (10 - 1) * progressao
print("Os primeiros termos dessa progressão são:")
c = termo
while c <= decimo:
    print(c, end=' -> ')
    c += progressao

print('Acabou')
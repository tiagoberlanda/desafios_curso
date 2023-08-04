# melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos, o programa encerra se ele disser que quer 0 termos
termo = int(input('Digite o termo da PA: '))
progressao = int(input('Digite a progressão da PA: '))
decimo = termo + (10 - 1) * progressao
print("Os primeiros termos dessa progressão são:")
c = termo

# Mostra os 10 primeiros termos
while c <= decimo:
    print(c, end=' -> ')
    c += progressao

print('\n')  # Pula uma linha após mostrar os primeiros 10 termos

# Pergunta ao usuário se deseja mostrar mais termos
while True:
    mais_termos = int(input('Deseja mostrar mais quantos termos? (Digite 0 para encerrar): '))
    if mais_termos == 0:
        break

    # Atualiza o valor de decimo para mostrar mais termos
    decimo += mais_termos * progressao
    c = c - progressao  # Reseta o contador para mostrar a partir do último termo mostrado anteriormente

    # Mostra os termos adicionais
    while c <= decimo:
        print(c, end=' -> ')
        c += progressao

print('Acabou')

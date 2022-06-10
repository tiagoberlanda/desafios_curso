'''Crie um programa que leia dois valores e mostre um menu na tela
[1]Somar, [2] Multiplicar, [3] Maior , [4] Novos Números [5] Sair do programa'''

## Variaveis ##
menu  = "[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos valores\n[5] Sair"
condicao1 = 0
condicao2 = 0

## Metodos ##
def somar(valor1,valor2):
    resultado = valor1 + valor2
    return resultado

def multiplicar(valor1,valor2):
    resultado = valor1 * valor2
    return resultado
    
def maior(valor1,valor2):
    if valor1 > valor2:
        resultado = valor1
    elif valor2 > valor1:
        resultado = valor2
    else:
        resultado = 'Nem Maior, Nem Menor!'
    return resultado

## Inicio ##
while condicao1 == 0:
    print('-=-' * 10)
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite mais um valor: '))
    condicao2 = 0   #Reseta o valor da condicao2 para evitar erro
    while condicao2 == 0:
        print(menu)
        escolha = int(input('Seleciona uma opção: '))
        
        if escolha == 1 :
            soma = somar(valor1,valor2)
            print('A soma entre {} e {} vale {}'.format(valor1,valor2,soma))
            
        elif escolha == 2:
            multiplca = multiplicar(valor1,valor2)
            print('O produto de {} com {} vale {}'.format(valor1,valor2,multiplca))
            
        elif escolha == 3:
            numero = maior(valor1,valor2)
            print('O maior valor entre {} e {} é {}'.format(valor1,valor2,numero))
            
        elif escolha == 4:
            print('-=-' * 10)
            condicao2 = 1
            
        elif escolha == 5:
            condicao1 = 1
            condicao2 = 1
        else:
            print('Você digitou um valor incorreto!\nDigite novamente!')
print('Fim')

# Crie um programa que leia vários números inteiros, e no final mostre a média entre todos os valores e qual foi o maior e o menor valor lidos, o programa também deve perguntar ao usuário se ele quer ou não continuar a digitar valores


numeros = []  # Lista para armazenar os números digitados
continuar = True

while continuar:
    try:
        numero = int(input('Digite um número inteiro: '))
        numeros.append(numero)

        opcao = input('Deseja continuar? (S/N): ')
        continuar = opcao.upper() == 'S'

    except ValueError:
        print("Digite um número inteiro válido.")

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("Nenhum número foi digitado.")


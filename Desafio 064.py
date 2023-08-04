# crie um programa que leia vários números inteiros, o programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final mostre quantos numeros foram digitados e a soma entre eles
total = 0
condicao = 0
while condicao == 0:
    valor = int(input('Digite um valor: '))
    if valor != 999:
        total += valor
    else:
        condicao = 1
print('A soma de todos os valores digitados é: ',total)

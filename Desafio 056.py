# Crie um programa que leia o nome, idade e sexo de 4 pessoas
# No final mostre a média de idade do grupo;
# Qual é o nome do Homem mais Velho.
# Quantas mulherem tem menos de 20 anos;
media = 0
soma = 0
nomeVelho = ''
maiorIdadeHomem = 0
totMulher20 = 0
for p in range(1,5):
    print('=-' * 10)
    nome = str(input('Digite o nome da {}° pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(p)))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p ==1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
    
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O Homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('O total de mulheres que possuem menos que 20 anos é {}'.format(totMulher20))

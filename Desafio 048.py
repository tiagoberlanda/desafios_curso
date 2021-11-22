# Criar um progrma que calcule a soma entre todos os números ímpares
# que são mútiplos de três a que estão no intervalo de 1 até 500
print('''A soma de todos os números impares
dívisiveis por 3 no intervalor de 1 e 500 são:''', end = " ")
soma = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
print(soma)

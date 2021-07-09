#Desenvolva um código que leia o peso e altura de uma pessoa, calcula seu IMC e mostre seu status
# de acordo com as seguintes condições
# abaixo de 18.5: abaixo do peso, entre 18.5 e 25 :Peso Ideal, 25 até 30: sobrepeso,30 até 40:obesidade
# acima de 40:obesidade mórbida
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = (peso / (altura * altura))
print('O Seu IMC vale {:.2f}'.format(imc))
if imc < 18.5:
    condicao = 'Abaixo do Peso'
elif imc >= 18.5 and imc < 25:
    condicao = 'Peso Ideal'
elif imc >= 25 and imc < 30:
    condicao = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    condicao = 'Obesidade'
elif imc >= 40:
    condicao = 'Obesidade Morbida'
print('Diante disso você está classificado como {}'.format(condicao))

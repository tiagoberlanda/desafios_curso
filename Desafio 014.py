# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura = float(input('Digite a temperatura em Celsius(°C): '))
far = (temperatura * 9/5) + 32
print('{}°C correspondem à {}°F'.format(temperatura, far))

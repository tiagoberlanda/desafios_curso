# Criar contagem regressiva para estourar os fogos de artifício
# Indo de 10 até 0 com uma pausa de 1s entre eles
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos Estourando!!')

# Faça um programa que leia um valor em metros e exiba o valor convertido em centímetros e milímetros.
metros = float(input('Digite o valor em metros: '))
# Continuando , mostre o valor de Quilometros, Hectometros, Decametros, decimetros centimetros e milimetros.
cm = metros * 100
mm = metros * 1000
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('{} metros equivalem à {} quilômetros, {} hectômetros, {} decâmetros'.format(metros, km, hm, dam))
print('E equivalem á {:.0f} decímetros, {:.0f} centimetros e {:.0f} milímetros.'.format(dm, cm, mm))

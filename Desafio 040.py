# Crie um programa que leia 2 notas de um aluno, calcule sua média e mostre uma mensagem no fim dizendo
# se ele foi aprovado (media maior que 7), recuperação( entre 5.0 e 6.9) ou reprovado (menor que 5.0)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media > 7.0:
    print('Você foi APROVADO com média {}, Parabéns'.format(media))
elif media <= 6.9 and media >= 5.0:
    print('Você ficou de RECUPERAÇÃO, sua média foi {}'.format(media))
else:
    print('Você foi REPROVADO, sua média foi {}'.format(media))

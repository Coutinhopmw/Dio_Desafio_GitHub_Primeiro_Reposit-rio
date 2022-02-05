# 025 AQUELE CLÁSSICO DA MÉDIA

nota1= float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7.0:
    print('Média final: {}, APROVADO'.format(media))
if media >= 5.0 and media <=6.9:
    print('Média final: {}, RECUPERAÇÃO'.format(media))
if media < 5.0:
    print('Média final: {}, REPROVADO'.format(media))

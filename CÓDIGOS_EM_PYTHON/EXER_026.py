# 026 Classificando atletas

idade = int(input('Informe a sua idade: '))

if idade <= 9:
    print('Categoria: MIRIM')

if  idade >= 10 and idade <= 14:
    print('Categoria: INFANTIL')

if idade >= 15 and idade <= 19:
    print('Categoria: JUNIOR')

if idade == 20:
    print('Categoria: SENIOR')

if idade > 20:
    print('Categoria: MASTER')


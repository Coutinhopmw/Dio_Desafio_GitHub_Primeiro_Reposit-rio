# 027 ANALISANDO OS TRIANGULOS V 2.0

import math

n1 = float(input('Informe o lado Direito: '))
n2 = float(input('Informe o lado Esquerdo: '))
n3 = float(input('Informe a base: '))

aux1 = n1 - n2
aux1 = abs(aux1) #Funcao retorna o numero absoluto
print(' aux1: {} '.format(aux1))
aux2 = n1 + n2
aux3 = n1 + n3
if( aux1 < n3 and aux2 >= n3 ):
    if( aux2 == aux3 ):
        print('O triangulo informado é: Equilátero')
    if( n1 == n2 or n1 < n3 ):
        print('O triangulo é: Isóceles')
    else: # Calculo realizado por esse else: aux2 <= aux3:
        print('O triangulo é: Escaleno')
else:
    print('Os valores informanos não são um triangulo')

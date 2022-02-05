#028 INDICE DE MASSA MARCOPORAL
import math
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

altura = pow(altura,2)

aux = peso/altura

if aux < 18.5:
    print('Voce esta abaixo do peso!')
if aux > 18.5 and aux < 25.0:
    print('Voce esta no peso ideal!')
if aux > 25.0 and aux < 30.0:
    print('Voce esta acima do peso!')
if aux > 30.0 and aux < 40.0:
    print('Voce esta obeso!')
if aux > 40.0:
    print('Voce esta com obesidade morbida!')

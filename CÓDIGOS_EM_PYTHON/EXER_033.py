# 033 soma dos pares

#n1 = int(input('Informe um valor 01: '))
#n2 = int(input('Informe um valor 02: '))
#n3 = int(input('Informe um valor 03: '))
#n4 = int(input('Informe um valor 04: '))
#n5 = int(input('Informe um valor 05: '))
#n6 = int(input('Informe um valor 06: '))
aux = 0
num = [0,0,0,0,0,0,0]
for i in range(1,7):
    num[i]= int(input('Insira o {} ° numero: '.format(i)))
for i in range(0,6):
    if num[i] % 2 == 0:
        aux = aux + num[i]

print('Soma dos numeros pares é: {}'.format(aux))


# 009 Tabuada

var = int(input('Informe um numero: '))
cont = var
i=1
while i <= 10:
    aux = var * i
    print('{} x {} = {}'.format(cont,i ,aux))
    i = i+1

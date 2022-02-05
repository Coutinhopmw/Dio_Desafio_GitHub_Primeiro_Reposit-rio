# 011 Calculo de metros quadrados

comp = float(input('Informe o comprimento: '))
larg = float(input('Informe a largura: '))
paint = 0.2

aux = comp * larg

print('Quantidade de mts quadrados: {}'.format(aux))

paint = int(comp/paint)

print('Quantide de tinta necessária: {}'.format(paint))

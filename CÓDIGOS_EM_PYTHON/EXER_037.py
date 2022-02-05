# 037 Grupo da maior idade

idade = [0000,0000,0000,0000,0000,0000,0000,0000]
ano_atual = 2021
aux1 = 0
aux2 = 0
for i in range(1,8):
    idade[i] = int(input('Informe a {}° idade: '.format(i)))

for i in range(0,7):
    if ano_atual- idade[i] > 18:
        aux1= aux1 + 1
    else:
        aux2 = aux2 + 1

print('{} passoas já atingiram a maior idade!'.format(aux1))
print('{} passoas não atingiram a maior idade!'.format(aux2))


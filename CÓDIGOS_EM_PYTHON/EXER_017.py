# 017 Catetos e hipotenusa
import math
cat_op = float(input('Informe o cateto oposto: '))
cat_adj = float(input('Informe o cateto adjasente: '))
cat_op = pow(cat_op,2)
cat_adj = pow(cat_adj,2)
aux = cat_op + cat_adj

print('Hipotenusa = {}'.format(aux))
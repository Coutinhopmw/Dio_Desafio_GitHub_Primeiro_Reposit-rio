# 032 SOMA ÍPARES MULTIPLOS DE 3

i = 0

for i in range(1,100):
    if (i % 3) == 0:
        print('Numero {} é multiplo de 3.'.format(i))
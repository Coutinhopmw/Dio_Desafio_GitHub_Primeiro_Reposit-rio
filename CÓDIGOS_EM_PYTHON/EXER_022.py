# 022 Coversor de bases numéricas

num = int(input('Informe um número: '))
resp = int(input('Digite: 1-Binário, 2-Octal, 3-Hexadecimal: '))

if resp == 1:
    resp = bin(num)
    print('Valor em Binário: {}'.format(resp))
elif resp == 2:
    resp =oct(num)
    print('O valor em Octal: {}'.format(resp))
elif resp == 3:
    resp = hex(num)
    print('O valor em Hexadecimal: {}'.format(resp))

# 015 Alugel de carros

dias = int(input('Informe a quantidade de Dias: '))
KMs = float(input("Informe a quantidade de KMs percorridos: "))
dias = dias * 60.00
KMs = KMs * 0.15
total = dias + KMs
print('Valor total: {}'.format(total))

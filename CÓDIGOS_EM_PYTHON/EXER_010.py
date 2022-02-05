# 010 Conversor de moedas
from decimal import Decimal
valor = float(input('Informe o valor em R$: '))

dolar = 5.70 # Cotacao do dolar em 18/12/21

valor = valor / dolar

print('Voce pode comprar {:.2f} dolares americanos.'.format(valor))


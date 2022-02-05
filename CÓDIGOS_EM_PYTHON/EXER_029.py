# 029 Gerenciador de pagamentos

var = float(input('Informe o valor do produto: '))
resp = int(input('Escolha forma de pagamento! \n'
      '1 - A vista/Cheque, 2 - A vista cartao, 3 - Em 2x, 4 - em 3x '))

if resp == 1:
    var = var - 0.10
    print('Valor com 10% de desconto: {}'.format(var))

if resp == 2:
    var = var - 0.05
    print('Valor com 05% de desconto: {}'.format(var))

if resp == 3:
    print('Valor normal: {}'.format(var))

if resp == 4:
    var = var + 0.20
    print('Valor com 20% de juros: {}'.format(var))

# 021 Aprovando Empréstimmo

val_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
qtd_anos = int(input('Informe a quantidade de anos para o pagamento : '))
qtd_anos = qtd_anos * 12

parcela = val_casa/qtd_anos
salario = salario * 0.30
print('Valor mensal das parcelas: {}'.format(parcela))

if parcela > salario:
    print('O impréstimo não foi aprovado!'
          'O valor exede os 30% do salário')

else:
    print('Parabéns! Seu impréstimo foi aprovado!')

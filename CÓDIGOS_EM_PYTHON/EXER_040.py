# 040 Validação de dados
resp = True
while resp == True:
    sexo = str(input('Informe o sexo: M/F '))
    if sexo == 'M' or sexo == 'F':
        print('Voce digitou o valor corretamente!')
        break
    else:
        print('ERRO! Digite apenas M/F')
        print('Digite novamente!')


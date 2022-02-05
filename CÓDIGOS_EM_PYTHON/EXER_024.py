# 024 ALISTAMENTO MILITAR

ano_nasc = int(input('Informe o ano do seu nascimento: '))
idade = (ano_nasc - 2022) * (-1)
print('{}'.format(idade))
if idade < 18 :
    aux = 18 - idade
    print('Idade insuficiente! Ainda faltam {} anos para que vc possa alistar-se'.format(aux))
if idade > 18 and idade <= 23:
    print('É hora de se alistar!')
if idade >= 24 :
    aux = idade - 18
    print('Idade exedita! Voce passou {} anos do prazo!'.format(aux))


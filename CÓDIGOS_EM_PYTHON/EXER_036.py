# 036 Palíndromo

nome= str(input('Digite uma palavra: '))

if str(nome) == str(nome)[::-1]:
    print('A palavra {} é um palíndromo!'.format(nome))
else:
    print('A palavra {} não é um palíndromo!'.format(nome))

print(nome)

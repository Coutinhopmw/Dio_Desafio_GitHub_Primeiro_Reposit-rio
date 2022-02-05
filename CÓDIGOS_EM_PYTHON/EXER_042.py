# 042 Valores unicos em uma lista

num = []

while True:
    aux = int(input('Digite um número: '))
    aux2 = str(input('Deseja inserir um novo valor ? S/N '))
    if aux2 == 'N':
        break
    num.append(aux)
num = sorted(num)
print(num)
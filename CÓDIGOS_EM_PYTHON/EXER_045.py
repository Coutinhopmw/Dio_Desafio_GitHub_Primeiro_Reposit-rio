lista_1= []
lista_2= []
lista_3= []
cont = 0
while True:
    aux = int(input('Digite um número: '))
    aux2 = str(input('Deseja inserir um novo valor ? S/N '))
    if aux2 == 'N':
        break
    lista_1.append(aux)
tam = len(lista_1)
for i in range(0,tam):
    if lista_1[i] % 2 == 0:
        lista_2[i] = lista_1[i]
    else:
        lista_3[i] = lista_1[i]
print('1ª Lista: {}'.format(lista_1))
print('2ª Lista: {}'.format(lista_2))
print('3ª Lista: {}'.format(lista_3))

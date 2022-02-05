# 041 Maior e menores valores na lista

lista = [0,0,0,0,0,0]

for i in range(0,5):
    lista[i] = int(input('Digite um numero: '))

lista= sorted(lista)
print('O numero é: {}, e está na posição 5'.format(lista[5]))
print('O menor numero é: {}, e está na posição 1'.format(lista[1]))

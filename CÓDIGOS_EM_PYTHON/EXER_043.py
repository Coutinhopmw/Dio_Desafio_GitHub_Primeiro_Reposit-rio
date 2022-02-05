# 043 Lista ordenada sem repetições

lista = [0,0,0,0,0]
for i in range(0,5):
    aux = int(input('Digite um numero: '))
    if aux < lista[i - 1]:
        lista[i] = aux
    else:
        lista[i + 1] = aux

print(lista)
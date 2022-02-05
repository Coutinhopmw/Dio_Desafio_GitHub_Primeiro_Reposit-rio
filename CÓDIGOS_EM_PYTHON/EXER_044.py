# 044 EXTRAINDO DADOS DE UMA LISTA

var= []
cont = 0
while True:
    aux = int(input('Digite um número: '))
    aux2 = str(input('Deseja inserir um novo valor ? S/N '))
    cont = cont + 1
    if aux2 == 'N':
        break
    var.append(aux)
var = sorted(var)
tam = len(var)
print(var)
print('Fora digitados {} numeros'.format(tam))
for i in range(0,tam):
    if var[i] == 5:
        print('O valor 5 está na lista e foi digitado')
    else:
        print('O valor 5 não está na lista e não foi digitado!')


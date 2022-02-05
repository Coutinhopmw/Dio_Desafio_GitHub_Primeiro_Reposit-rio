# 020 SORTEANDO UMA ORDEM NA LISTA
import random
i = 1
lista = [[10], [10], [10], [10]],
while i <= 4:
    lista = str(input('Informe o nome do aluno {}: '.format(i)))
    i = i + 1
resp = 1
while resp < 4:
    resp = random.randint(1,4)
    print('{}'.format(lista[resp]))


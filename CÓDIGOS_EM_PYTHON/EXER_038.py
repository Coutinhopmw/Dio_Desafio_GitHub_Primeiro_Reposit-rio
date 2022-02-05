# 038 Maior e menor da sequencia

peso = [00000,00000,00000,00000,00000,00000]

for i in range(1,6):
    peso[i] = float(input('Informe o peso da {}ª pessoa: '.format(i)))

peso= sorted(peso)
print('O maior peso foi: {:.3f}'.format(peso[5]))
print('O menor peso foi: {:.3f}'.format(peso[1]))
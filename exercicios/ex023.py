n1 = int(input('Digite um número de 0 à 9999: '))
un = n1 // 1 % 10
de = n1 // 10 % 10
ce = n1 // 100 % 10
mi = n1 // 1000 % 10
print ('Analisando o número {}'.format(n1))
print('Valor de unidade: {}'.format(un))
print('Valor de dezena: {}'.format(de))
print('Valor de centena: {}'.format(ce))
print('Valor de milhar: {}'.format(mi))
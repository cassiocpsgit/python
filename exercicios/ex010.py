n1 = float(input('Quantos reais você tem? '))
n2 = float(input('Qual a cotação do dolar hoje? '))
n3 = n1 / n2
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(n1, n3))

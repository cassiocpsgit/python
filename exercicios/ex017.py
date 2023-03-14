'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hi))'''
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
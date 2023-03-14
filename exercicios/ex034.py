s = float(input('Qual o salário do funcionário? R$'))
'''a = 0.1
b = 0.15
if s <= 1250:
    print('Para este funcionário o valor do novo salário será R${:.2f}.'.format(s + s * b))
else:
    print('Para este funcionário o valor do novo salário será R${:.2f}.'.format(s + s * a))'''
if s <= 1250:
    novo = s + s * 0.15
else:
    novo = s + s * 0.10
print('O novo valor do salário deste funcionário será \033[1;31;107mR${:.2f}\033[m.'.format(novo))



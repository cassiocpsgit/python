'''tempo = int(input('Quanto anos tem seu carro? '))
print('Carro novo.' if tempo <= 3 else 'Carro velho')
print('--FIM--')'''


tempo = int(input('Quanto anos tem seu carro? '))
if tempo <= 2:
    print('Seu carro é novo.')
else:
    print('Seu carro é velho.')
print('--FIM--')
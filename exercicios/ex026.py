frase = input('Digite uma frase: ').upper().strip()
print('A letra "A" aparece {} vezes nesta frase.'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra "A" aparece na posição {}.'.format(frase.rfind('A')+1))
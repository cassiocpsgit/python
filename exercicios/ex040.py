n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
    print('Sua média foi {:.2f}, portanto você está reprovado!'.format(media))
elif media >= 7:
    print('Sua média foi {:.2f}, portanto você está aprovado!'.format(media))
else:
    print('Sua média foi {:.2f}, portanto você está de recuperação!'.format(media))

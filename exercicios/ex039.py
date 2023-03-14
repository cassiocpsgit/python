from datetime import date
atual = date.today().year
dn = int(input('Em que ano você nasceu?'))
idade = atual - dn
print('Quem nasceu em {} tem ou terá {} anos em {}.'.format(dn, idade, atual))
if idade < 18:
    print('Portanto você ainda ainda não precisa se alistar.')
elif idade > 18:
    print('Portanto seu período de alistamento já passou.')
else:
    print('Portanto você deve se alistar imediatamente.')
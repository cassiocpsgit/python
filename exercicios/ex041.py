from datetime import date
atual = date.today().year
dn = int(input('Digite o ano de nascimento: '))
id = atual - dn
if id < 9:
    print('Voce tem {} anos e sua categoria é MIRIM.'.format(id))
elif 9 <= id < 14:
    print('Voce tem {} anos e sua categoria é INFANTIL.'.format(id))
elif 14 <= id < 19:
    print('Voce tem {} anos e sua categoria é JUNIOR.'.format(id))
elif 19 <= id < 25:
    print('Voce tem {} anos e sua categoria é SÊNIOR.'.format(id))
elif 25 <= id:
    print('Voce tem {} anos e sua categoria é MASTER.'.format(id))
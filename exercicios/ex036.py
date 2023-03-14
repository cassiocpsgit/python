vlc = float(input('Qual é o valor da casa?'))
sal = float(input('Qual é o seu salário?'))
prc = int(input('Qual o número de parcelas?'))
prest = vlc / prc
if prest <= sal * 0.3:
    print('O empréstimo foi autorizado.')
else:
    print('O empréstimo foi negado.')

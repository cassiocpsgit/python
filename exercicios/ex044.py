print('{:=^50}'.format(' LOJAS CASSIOTECH '))
preço = float(input('Digite o valor total da compra: '))
print('''\nFORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque. 10% de desconto.
[2] À vista no cartão. 5% de desconto.
[3] Em até 2x no cartão. Preço normal.
[4] 3x ou mais no cartão. 20% de juros.''')
opção = int(input('\nEscolha uma forma de pagamento: '))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif opção == 4:
    total = preço + preço * 0.2
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

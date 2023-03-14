n = int(input('digite um número: '))
for c in range(1, 11):
    print('{:2} x {:2} = {}'.format(n, c, c * n))
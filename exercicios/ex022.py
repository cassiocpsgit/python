nome = input('Qual é o seu nome?\n').strip()
divisao = nome.split()
pnome = divisao[0]
print(nome.upper())
print(nome.lower())
print('Seu nome inteiro tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(pnome)))
#Cassio Cortez Pereira da Silva
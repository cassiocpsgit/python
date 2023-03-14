import emoji
#Cassio Cortez Pereira da Silva
n = input('Digite seu nome completo: ').strip()
nome = n.split()
print('Muito prazer em te conhecer{}!'.format(emoji.emojize(':thumbs_up:')))
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[-1]))
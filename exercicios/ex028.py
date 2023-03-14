import emoji
from random import randint
from time import sleep
c = randint(0, 5)
print('-=-' *18)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *18)
j = int(input('Em que número eu pensei?\n'))
print('PROCESANDO...')
sleep(1)
print('Eu pensei no número {}.'.format(c))
if j == c:
    print('Parabéns, você acertou{}!!!'.format(emoji.emojize(':trophy:')))
else:
    print('Você errou. Tente novamente{}.'.format(emoji.emojize(':disappointed_face:')))
print('FIM')

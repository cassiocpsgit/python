n = input('Qual é o seu nome?')
i = input('Qual é a sua idade?')
p = float(input('Qual é o seu peso?'))
a = float(input('Qual é a sua altura?'))
imc = p / a ** 2
print('Olá {}, bom dia!\nO seu IMC é {:.2f}.'.format(n, imc))
if imc < 18.5:
    print('Você está magro!')
if imc >= 18.5 and imc <= 24.9:
    print('Você está saudável!')
if imc >= 25 and imc <= 29.9:
    print('Você está com sobrepeso!')
if imc >= 30:
    print('Você está obeso!')
import random
pc=random.randint(1,5)

print('Vamos jogar um jogo de adivinhação!')
user=int(input('Diga-me um valor de 1 a 5: '))
if pc==user:
    print('Parabéns, vocês escolheu o mesmo número que o computador! ')
else:
    print('Você erro, tente novamente!')
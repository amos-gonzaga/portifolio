print('Vamos jogar Jo-ken-po!')
jogada=int(input('Escolha 1 para Pedra; 2 para Papel; 3 para Tesoura!'))
import random
contra=random.randint(1,3)
if jogada==contra:
    print('Você e a máquina jogaram a mesma coisa, jogue novamente!')
if jogada==1 and contra==2:
    print('Papel cobre pedra, você perdeu!')
if jogada==1 and contra==3:
    print ('Pedra quebra tesoura, você ganhou!')
if jogada==2 and contra==1:
    print('Papel cobre pedra, você venceu!')
if jogada==2 and contra==3:
    print('Tesoura corta papel, você perdeu!')
if jogada==3 and contra==1:
    print('Pedra quebra tesourada, você perdeu!')
if jogada==3 and contra==2:
    print('Tesoura corta papel, você venceu!')
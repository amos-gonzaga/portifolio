print('Essa aplicação contará de 30 até 0 de trás pra frente e marcará os números que forem divisíveis por 4.')
cont=30
while cont>-1:
    if (cont%4==0):
        print('[',cont,']')
        cont-=1
    else:
        print(cont)
        cont-=1
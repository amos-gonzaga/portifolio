print('Essa aplicação é um contador complexo.')
aux=0
inicio=int(input('Diga-me o primeiro número da contagem: '))
fim=int(input('Diga-me o fim da contagem: '))
inc=int(input('Diga-me o valor de incremento: '))
if inicio<fim:
    while inicio<fim:
        print(inicio)
        inicio+=inc
else:
    while fim<inicio:
        print(fim)
        fim-=inc



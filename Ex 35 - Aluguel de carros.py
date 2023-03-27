print('Essa aplicação avaliará os custos do aluguel de carros.')
tcarro=0
tcarro = int(input('Você prefere um carro popular ou um carro de luxo? Digite 1 para carro popular e 2 para carro de luxo.'))
while tcarro<1 or tcarro>2:
    if tcarro < 1 or tcarro > 2:
        print('Você escolheu uma opção indisponível.')
        tcarro = int(input('Você prefere um carro popular ou um carro de luxo? Digite 1 para carro popular e 2 para carro de luxo.'))
dias=int(input('Diga-me quantos dias você prentende ficar com o carro: '))
dist=int(input('Diga-me quantos km você rodará com o carro: '))
if tcarro==1:
    if dist>100:
        preco=(dist*0.1)+(dias*90)
    else:
        preco=(dist*0.2)+(dias*90)
if tcarro==2:
    if dist>200:
        preco=(dist*0.25)+(dias*150)
    else:
        preco=(dist*0.3)+(dias*150)
print('Você pagará no aluguel desse carro e nessas condições o valor de ',round(preco,2),' R$.')

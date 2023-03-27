print('Hoje é dia de promoção especial do Dia das Mulheres na Magalu.')
nome=(input('Diga-me seu nome por favor: '))
sexo=str(input('Diga-me o seu sexo: [H/M]'))
valor=float(input('Diga-me o valor das suas compras: '))
if sexo=='M':
    desconto=(valor/100)*87
    print(nome, ', sua compra ficou no total de ', desconto, ' R$.')

if sexo=='H':
    desconto=(valor/100)*95
    print(nome, ', sua compra ficou no total de ', desconto, ' R$.')

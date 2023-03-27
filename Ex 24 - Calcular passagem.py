dist=int(input('Diga-me a distância em KM que você deseja percorrer: '))
preco=0
if (dist>200):
    preco=dist*0.45
else:
    preco=dist*0.5
print('Você terá de pagar', preco,'R$.')
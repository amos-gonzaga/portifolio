print('Esse app aplicará um desconto de 5% na mercadoria comprada.')
preco=float(input('Diga-me o valor da mercadoria: '))
desc=float((preco/100)*95)
apoio=desc
apoio=round(apoio, 3)

print('O preço final será de ',apoio)
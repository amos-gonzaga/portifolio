print('Esse é o programa avaliativo da Imobiliária Gaspari.')
print('Você deseja comprar uma casa e nos iremos avaliar se a venderemos a você a partir de nossos parâmetros.')
casa=float(input('Diga-me o valor da casa em reais: '))
salario=float(input('Agora diga-me seu salário: '))
anos=int(input('Agora diga-me em quantos anos pretende pagar essa casa: '))
meses=anos*12
parcela=casa/meses
if parcela>((salario/100)*30):
    print('A venda foi negada por que a parcela supera 30% do seu salário.')
else:
    print('A venda foi aprovada e você pagara ',parcela,' R$ mensalmente.')

nome=input('Diga-me o nome do funcionário: ')
sal=float(input(f'Diga-me o salário do {nome}:'))
anos=int(input(f'Diga-me a quantos anos {nome} trabalha na empresa: '))
if anos>10:
    nsal=sal*1.2
elif anos>3 and anos<10:
    nsal=sal*1.125
else:
    nsal=sal*1.03
print(f'O novo salário de {nome} é igual a {nsal} R$.')
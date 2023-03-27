print('Essa aplicação calcula o custo de tinta para se pintar uma parede.')
alt=float(input('Diga-me a altura em metros da parede: '))
larg=float(input('Diga-me a largura em metros da parede: '))
area=alt*larg
tinta=area/2
print('A área a ser pintada é igual a ',area,' metros quadrados e serão necessários ',tinta,' litros de tinta.')
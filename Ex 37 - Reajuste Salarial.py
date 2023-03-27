print('Essa aplicação calculará o reajuste salarial do funcionariado.')
anos=int(input('Diga-me a quantos anos você trabalha na empresa: '))
sal=float(input('Diga-me seu salário atual: '))
gen=0
gen=int(input('Diga-me seu gênero, sendo 1 para mulher e 2 para homem: '))
while gen<1 or gen>2:
    if gen < 1 or gen > 2:
        print('Você escolheu uma opção indisponível.')
        gen = int(input('Diga-me seu gênero, sendo 1 para mulher e 2 para homem: '))
if gen==1:
    if anos>20:
        nsal=(sal*1.23)
    elif anos>15:
        nsal=(sal*1.12)
    else:
        nsal=(sal*1.05)
if gen==2:
    if anos>30:
        nsal=(sal*1.25)
    elif anos>20:
        nsal=(sal*1.13)
    else:
        nsal=(sal*1.03)
print('Seu novo salário é igual a ',round(nsal,2)," R$.")

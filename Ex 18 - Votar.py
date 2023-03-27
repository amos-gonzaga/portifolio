ano=int(input('Diga-me o ano em que você nasceu: '))
idade=2023-ano
if idade>16:
    print('Você tem ',idade,' anos de idade e já pode votar.')
else:
    print('Você tem',idade,' anos e ainda não pode votar.')
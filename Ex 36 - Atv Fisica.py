print('Essa aplicação lhe dará pontos conforme suas atividades físicas.')
atv=int(input('Diga-me quantas horas de exercícios físicos você pratica por mês: '))
if atv>20:
    pontos=atv*10
elif atv>10:
    pontos=atv*5
else:
    pontos=atv*2
saldo=pontos*0.05
print('Com suas atividades físicas você ganhou um total de ',pontos,' e receberá ',saldo,' R$ como bonificação.')
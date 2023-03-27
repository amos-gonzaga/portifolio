n1=int(input('Diga-me a largura do terreno em metros: '))
n2=int(input('Diga-me o comprimento do terreno em metros: '))
area=(n1*n2)
if area>500:
    print(f'O terreno é VIP tem {area} m² de área.')
elif area>100 and area<500:
    print(f'O terreno é MASTER tem {area} m² de área.')
else:
    print(f'O terreno é POPULAR tem {area} m² de área.')
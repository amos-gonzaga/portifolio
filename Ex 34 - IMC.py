print('Essa aplicação calculará seu IMC.')
alt=float(input('Diga-me sua altura em metros: '))
peso=float(input('Diga-me seu peso em kg: '))
imc=peso/(alt**2)
print('Seu IMC é igual a ', round(imc))
if imc>40:
    print('Você está com obesidade mórbida.')
elif imc>30:
    print('Você está com obesidade.')
elif imc>25:
    print('Você está com sobrepeso.')
elif imc>18.5:
    print('Você está com o peso ideal.')
else:
    print('Você está abaixo do peso.')
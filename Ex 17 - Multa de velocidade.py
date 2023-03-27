velocidade=int(input('Diga-me a velocidade do seu carro: '))
if velocidade>80:
    print('Você foi multado! O valor da multa é igual a ',(velocidade-80)*5,' R$.')
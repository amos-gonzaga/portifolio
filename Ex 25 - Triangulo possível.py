print('Tentaremos montar um triângulo com os números que você nos dará.')
l1=float(input('Diga-me um número: '))
l2=float(input('Diga-me outro número: '))
l3=float(input('Diga-me mais um número: '))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('O triângulo é possível.')
else:
    print('O triângulo não é possível. ')

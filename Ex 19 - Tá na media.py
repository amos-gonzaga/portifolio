nome=input('Diga-me seu nome: ')
n1=float(input('Diga-me sua primeira nota: '))
n2=float(input('Diga-me sua segunda nota: '))
media=(n1+n2)/2
if media>7:
    print('Seu aproveitamento foi bom, com média de ',media,' pontos.')
else:
    print('Seu aproveitamento foi ruim, com média de ',media,' pontos.')
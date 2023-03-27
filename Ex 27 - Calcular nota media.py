n1=int(input('Diga-me a primeira nota do aluno: '))
n2=int(input('Diga-me a segunda nota do aluno: '))
media=(n1+n2)/2
if media>7:
    print('O aluno foi aprovado com média ',media)
elif media>5 and media<6.9:
    print('O aluno está de recuperação com media ', media)
else:
    print('O aluno foi reprovado. ')
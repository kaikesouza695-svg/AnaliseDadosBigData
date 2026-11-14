for alunos in range(1,11):

    nota1 = float(input("digite sua primeira nota:"))
    nota2= float(input("digite sua segunda nota:"))
    nota3 = float(input("digite sua terceira nota:"))
    nota4 = float(input("digite sua quarta nota:"))

    media =(nota1 +nota2+ nota3 + nota4) / 4

    print("media", round(media,3))

    if media>= 7:
        print("aprovado")

    elif media >5 <7:
        print("fazer recuperção")

    else:
        media <=5
        print("reprovado")
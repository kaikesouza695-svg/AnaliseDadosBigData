resultado=[]

for i in range(5):
    nota1 = float(input("digite sua nota:"))
    nota2 = float(input("digite sua nota:"))

    media = (nota1 + nota2) / 2
    if media >=7:
        situacao = "aprovado"

    else:
        situacao = "reprovado"

    resultado.append(f"aluno{i + 1} - {situacao}")

print("\nresultado:")
print(resultado)

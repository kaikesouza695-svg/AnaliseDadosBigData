candidatos = []

for i in range(5):
    nome = input("digite o seu nome:")
    email = input("digite seu email:")
    idade = int(input("digite sua idade:"))

    if idade>=18:
        candidato ={"nome": nome, "idade": idade, "email": email}
        candidatos.append(candidato)
        print("candidatos aprovado para cadastro!")
    else:
        print("cadidatos rejeitados para cadastro")

print("\ncandidatos:")
print(candidatos)
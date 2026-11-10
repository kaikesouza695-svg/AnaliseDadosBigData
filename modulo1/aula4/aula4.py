# uso da match case
#######

categorias = ["massas", "bebidas", "petiscos", "doces", "salgados", "pizza"
              "churrasco", "lanches," "comida japonesa", "pastel"]
print(categorias)

pergunta = input("escolha uma das categorias abaixo:")

match pergunta:
    case "massas":
        print("dia de massas, com rodizio e descontos é toda quarta feira")
    case "bebidas":
        print("dia de bebidas, com rodizio e descontos é toda quarta feira")
    case "doces":
        print("dia de bebidas, com rodizio e descontos é toda quarta feira")
    case "pizza":
        print("dia de pizza, com rodizio e descontos é toda quarta feira")
    case _:
        print("categoria não encontrada.")



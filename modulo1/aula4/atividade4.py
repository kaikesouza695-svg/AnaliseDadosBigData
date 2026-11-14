codigo = int(input("digite o seu codigo:"))

match codigo:
    case 1:
        print("sul")
    case 2:
        print("norte")
    case 3:
        print("leste")
    case 4:
        print("oeste")
    case 5:
        print("nordeste")
    case 6:
        print("suldeste")
    case 7:
        print("centro-oeste")
    case 8:
        print("noroeste")

    case _:
        print("produto importado")
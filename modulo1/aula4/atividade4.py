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
    case 5 | 6:
        print("nordeste")
    case 7|8|9:
        print("suldeste")
    case 10:
        print("centro-oeste")
    case 11:
        print("noroeste")

    case _:
        print("produto importado")
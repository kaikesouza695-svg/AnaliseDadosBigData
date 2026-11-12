contador = 3
limite = 0



while True:
    if contador >= limite:
        break 

    login = "kaike"
    senha = "2007"

    login_usuario=input("digite o seu nome:")
    senha_usuario=input("digite sua senha:")

    if login_usuario == login or senha_usuario == senha:
        print("clique para continuar")

    else:
        login_usuario == "" or senha_usuario == ""
        print("senha ou login invalidos. tente novamente!")

        contador = contador-1



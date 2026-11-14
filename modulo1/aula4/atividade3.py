inicio = float(input("digite o inicio do odometro:"))
fim = float(input("digite o final do odometro:"))
litros = float(input("quantos litros gastou?"))
recebido = float(input("digite o valor recebido:"))

distancia = fim - inicio
consumo = distancia / litros
combustivel = litros * 6.15
lucro = recebido - combustivel

if litros >0:
    print("distancia percorrida:", distancia, "km")
    print("media de consumo:", consumo, "km/l")
    print("gasto de combustivel:R$", combustivel)
    print("lucro liquido:R$", lucro)

else:
    print("quantidade de litros invalida")

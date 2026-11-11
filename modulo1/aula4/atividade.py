import math


potencia = 3
largura = 3
comprimento = 3

area = largura * comprimento

potencia_necessaria = area * 3

lampadas = potencia_necessaria * potencia

if lampadas % 1 !=0:
    lampadas = int(lampadas)+1
else:
    lampadas = int(lampadas)

print("area do comodo:", area, "m²" )
print("potencia necessaria:", potencia_necessaria, "w'")
print("lampadas necessarias:", lampadas)



numero1 = float(    
    input("primeiro número: ")
)
numero2 = float(    
    input("segundo numero: ")
)
operacao = input(   
    "operação (+, -, *, /): "
)
if operacao == "+": 
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao =="/":
    resultado = numero1 / numero2
else:
    resultado = "resultado inválido" 
print(resultado)

